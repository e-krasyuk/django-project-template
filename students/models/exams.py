from django.db import models
from django.utils.translation import ugettext_lazy as _

class Exam(models.Model):
	"""Exam Model"""

	class Meta(object):
		verbose_name = _(u'Exam')   
		verbose_name_plural = _(u'Exams')

	subject = models.CharField(
		max_length=256,
		blank=False,        #If True - field can be empty
		verbose_name=_(u"Subject Title"))

	date = models.DateTimeField(
		max_length=256,
		blank=False,
		verbose_name=_(u"Date and time"))

	teacher = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=_(u'Teacher'))

	exam_group = models.ForeignKey('Group',
		max_length=256,
		blank=False,
		verbose_name=_(u'Group'))


	def __unicode__(self):
		return u"%s" % (self.subject)
	