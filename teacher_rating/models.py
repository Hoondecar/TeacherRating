from uuid import uuid4

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.conf import settings
from django.db.models.aggregates import (
    Avg
)
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Chair(models.Model):
	title = models.CharField(max_length=200)
	def __str__(self):
		return '{}'.format(self.title)
	class Meta:
		verbose_name_plural = 'Кафедры'
		verbose_name = 'Кафедра'
		ordering = ['title']


"""def teacher_directory_path_with_uuid(instance, filename):
	return '{}/{}'.format(instance.teacher_id, uuid4())

class TeacherImage(models.Model):
	image = models.ImageField(
		upload_to=teacher_directory_path_with_uuid)
	uploaded = models.DateTimeField(
		auto_now_add=True)
	teacher = models.ForeignKey(
		'Teacher', on_delete=models.CASCADE)
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE)"""


class TeacherManager(models.Manager):
    def all_with_related_persons_and_score(self):
        qs = self.get_queryset()
        qs = qs.annotate(score=Avg('vote__value'))
        return qs

class Teacher(models.Model):
	name = models.CharField(max_length=30)
	lastname = models.CharField(max_length=50)
	patronymic = models.CharField(max_length=75, null=True)
	post = models.CharField(max_length=100)
	desription = models.TextField(null=True, blank=True)
	rating = models.IntegerField(max_length=10, null=True)
	chair = models.ForeignKey(Chair, on_delete=models.CASCADE)
	picture = models.ImageField(default="deafault.png")

	objects = TeacherManager()

	def __str__(self):
		return '{}  {} {}'.format(
			self.lastname, self.name, self.patronymic)

	class Meta:
		verbose_name_plural = 'Преподаватели'
		verbose_name = 'Прeподаватель'
		ordering = ['chair']

class VoteManager(models.Manager):

	def get_vote_or_unsaved_blank_vote(self, teacher, user):
		try:
			return Vote.objects.get(
				teacher=teacher,
				user=user)
		except Vote.DoesNotExist:
			return Vote(
				teacher=teacher,
				user=user)

class Vote(models.Model):
	ONE = 1
	TWO = 2
	THREE = 3
	FOUR = 4
	FIVE = 5
	VALUE_CHOICES = (
        (ONE, "⭐",),
        (TWO, "⭐⭐",),
        (THREE, "⭐⭐⭐"),
        (FOUR, "⭐⭐⭐⭐"),
        (FIVE, "⭐⭐⭐⭐⭐")
    )
	value = models.SmallIntegerField(choices=VALUE_CHOICES,)
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE)
	teacher =models.ForeignKey(
		Teacher,
		on_delete=models.CASCADE)
	voted_on = models.DateTimeField(
		auto_now=True)

	objects = VoteManager()

	class Meta:
		unique_together=('user', 'teacher')


class Comment(models.Model):
	class Meta:
		db_table = "comments"

	teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField('Комментарий')
	created_date = models.DateTimeField('Дата комментария', auto_now=True)
	approved_comment = models.BooleanField(default=True)

	def __str__(self):
		return self.text


	def approve(self):
		self.approved_comment = True
		self.save()




"""class TeacherManager(models.Manager):
	for teacher in Teacher.all"""

