from django import forms
from django.contrib.auth import \
    get_user_model

from teacher_rating.models import Vote, Teacher, Comment#,TeacherImage

"""class TeacherImageForm(forms.ModelForm):
	teacher = forms.ModelChoiceField(
		widget=forms.HiddenInput,
		queryset=Teacher.objects.all(),
		disabled=True)
	user = forms.ModelChoiceField(
		widget=forms.HiddenInput,
		queryset=get_user_model().objects.all(),
		disabled=True)

	class Meta:
		model = TeacherImage
		fields = ('image', 'user', 'teacher')"""

class VoteForm(forms.ModelForm):
	user = forms.ModelChoiceField(
		widget=forms.HiddenInput,
		queryset=get_user_model().objects.all(),
		disabled=True)
	teacher = forms.ModelChoiceField(
		widget=forms.HiddenInput,
		queryset=Teacher.objects.all(),
		disabled=True
		)
	value = forms.ChoiceField(
		label='Выберите оценку',
		widget=forms.RadioSelect,
		choices=Vote.VALUE_CHOICES,
		)


	class Meta:
		model = Vote
		fields = (
			'value', 'user', 'teacher',)

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('text',)

