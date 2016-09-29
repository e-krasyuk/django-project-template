# -*- coding: utf-8 -*-

from django.db import models

class Exam(models.Model):
	"""Exam Model"""

	class Meta(object):
		verbose_name = u'Іспит'   #Изменил название модели в Django admin
		verbose_name_plural = u'Іспити'

	subject = models.CharField(
		max_length=256,
		blank=False,        #При True поле может быть пустым
		verbose_name=u"Назва Предмету")

	date = models.DateTimeField(
		max_length=256,
		blank=False,
		verbose_name=u"Дата і час")

	teacher = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u'Викладач')

	exam_group = models.ForeignKey('Group',
		max_length=256,
		blank=False,
		verbose_name=u'Група')


	# Изменяю названия экзаменов в списке студентов Djanhgo admin
	def __unicode__(self):
		return u"%s" % (self.subject)
	