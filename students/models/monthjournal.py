from django.db import models
from django.utils.translation import ugettext_lazy as _


class MonthJournal(models.Model):
    """Student Monthly Journal"""

    class Meta:
        verbose_name = _(u'Month Journal')
        verbose_name_plural = _(u'Month Journals')

    student = models.ForeignKey('Student',
        verbose_name=_(u'Student'),
        blank=False,
        unique_for_month='date')
    # we only need year and month, so always set day to first day ofthe month
    date = models.DateField(
        verbose_name=_(u'Date'),
        blank=False)


    scope = locals()
    for field_num in range(1, 32):
        scope['present_day' + str(field_num)] = models.BooleanField(
            verbose_name=_(u'Day #') + str(field_num), default=False)

    def __unicode__(self):
        return u'%s: %d, %d' % (self.student.last_name, self.date.month, self.date.year)