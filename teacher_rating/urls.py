from django.urls import path

from . import views

app_name = 'teacher_rating'

urlpatterns = [
	path('search', views.SearchView.as_view(), name='Search'),
	path('teachers', 
		views.TeacherList.as_view(),
		name='teacher_list'),
	path('teacher/<int:pk>',
		views.TeacherDetail.as_view(),
		name='teacher_detail'),
	path('chairs', views.existing_chair, name='existing_chair'),
	path('chair/<chair_id>', views.by_chair, name='by_chair'),
	path('teacher/<int:teacher_id>/vote',
		views.CreateVote.as_view(),
		name='CreateVote'),
	path('teacher/<int:teacher_id>/vote/<int:pk>',
		views.UpdateVote.as_view(),
		name='UpdateVote'),
	path('teacher/<int:pk>/comment/', views.add_comment, name='add_comment'),
	path('', views.MainView, name='main')
]