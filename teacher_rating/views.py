from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import (
    LoginRequiredMixin)
from django.core.exceptions import (
    PermissionDenied)
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from teacher_rating.models import Teacher, Chair, Vote, Comment
from teacher_rating.forms import VoteForm, CommentForm#, TeacherImageForm
from django.http import HttpResponse
from django.views.generic import (
    ListView, DetailView, UpdateView,
    CreateView, View
)

def MainView(request):
    return render(request, 'teacher_rating/main.html')

class SearchView(View):
    template_name = 'teacher_rating/search.html'
    def get(self, request, *args, **kwargs):
        context = {}

        question = request.GET.get('q')
        if question is not None:
            search_teacher = Teacher.objects.filter(lastname=question.title())
            if search_teacher:
                context = {'teacher_lists':search_teacher}
                return render(request, 'teacher_rating/search.html', context)
            else:
                search_teacher = Teacher.objects.filter(name=question.title())
                if search_teacher is not None:
                    context = {'teacher_lists':search_teacher}
                    return render(request, 'teacher_rating/search.html', context)


class  TeacherList(ListView):
	model = Teacher

class TeacherDetail(DetailView):
    model=Teacher
    queryset = Teacher.objects.all_with_related_persons_and_score()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            vote = Vote.objects.get_vote_or_unsaved_blank_vote(
                teacher=self.object,
                user=self.request.user
            )
            if vote.id:
                vote_form_url = reverse(
                    'teacher_rating:UpdateVote',
                    kwargs={
                        'teacher_id': vote.teacher.id,
                        'pk': vote.id})
            else:
                vote_form_url = (
                    reverse(
                        'teacher_rating:CreateVote',
                        kwargs={
                            'teacher_id': self.object.id}
                    )
                )
            vote_form = VoteForm(instance=vote)
            ctx['vote_form'] = vote_form
            ctx['vote_form_url'] = \
                vote_form_url
            teacher_id = self.object.id
            comments = Comment.objects.filter(teacher_id=teacher_id).order_by('-created_date')
            voter=Vote.objects.filter(teacher=teacher_id)
            ctx['vote'], ctx['user_id'] = self.users_value(comments, voter)
            ctx['comments'] = comments
        return ctx

    def users_value(self,comments, voter):
        users_vote = {}
        user_id = 0
        for comment in comments:
            try:
                users_vote[comment.user_id.id] = voter.filter(user=comment.user_id)[0].value
                user_id = comment.user_id.id
            except:
                return users_vote, user_id
        return users_vote, user_id




def add_comment(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    user_id = request.user
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.teacher_id = teacher
            comment.user_id = user_id
            comment.save()
            return redirect('teacher_rating:teacher_detail', pk=teacher.pk)
    else:
        form = CommentForm()
    return render(request, 'teacher_rating/add_comment.html', {'form': form})




    """def teacher_image_form(self):
        if self.request.user.is_authenticated:
            return TeacherImageForm()
        return None"""

class UpdateVote(LoginRequiredMixin, UpdateView):
    form_class = VoteForm
    queryset = Vote.objects.all()

    def get_object(self, queryset=None):
        vote = super().get_object(
            queryset)
        user = self.request.user
        if vote.user != user:
            raise PermissionDenied(
                'cannot change another '
                'users vote')
        return vote

    def get_success_url(self):
        teacher_id = self.object.teacher.id
        return reverse(
            'teacher_rating:teacher_detail',
            kwargs={'pk': teacher_id})

    def render_to_response(self, context, **response_kwargs):
        teacher_id = context['object'].id
        teacher_detail_url = reverse(
            'teacher_rating:teacher_detail',
            kwargs={'pk': teacher_id})
        return redirect(
            to=teacher_detail_url)

class CreateVote(LoginRequiredMixin, CreateView):
    form_class = VoteForm

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user.id
        initial['teacher'] = self.kwargs[
            'teacher_id']
        return initial

    def get_success_url(self):
        teacher_id = self.object.teacher.id
        return reverse(
            'teacher_rating:teacher_detail',
            kwargs={'pk': teacher_id})

    def render_to_response(self, context, **response_kwargs):
        teacher_id = context['object'].id
        teacher_detail_url = reverse(
            'teacher_rating:teacher_detail',
            kwargs={'pk': teacher_id})
        return redirect(
            to=teacher_detail_url)
		
class ChairList(ListView):
	model = Chair

class ChairDetail(DetailView):
	model = Chair


def by_chair(request, chair_id):
	teachers = Teacher.objects.filter(chair=chair_id)
	chairs = Chair.objects.all()
	current_chair = Chair.objects.get(pk=chair_id)
	context = {'teachers':teachers, 'chairs':chairs,
				'current_chair':current_chair}
	return render(request, 'teacher_rating/chair_list.html', context)

def existing_chair(request):
	chairs = Chair.objects.all()
	context = {'chairs':chairs}
	return render(request, 'teacher_rating/chairs.html', context)



def index(request) :
	return HttpResponse("Здecь будет выведен список объявлений.")

