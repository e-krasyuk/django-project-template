# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20161015_1623'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exam',
            options={'verbose_name': 'Exam', 'verbose_name_plural': 'Exams'},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Group', 'verbose_name_plural': 'Groups'},
        ),
        migrations.AlterModelOptions(
            name='monthjournal',
            options={'verbose_name': 'Month Journal', 'verbose_name_plural': 'Month Journals'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Student', 'verbose_name_plural': 'Students'},
        ),
        migrations.AlterField(
            model_name='exam',
            name='date',
            field=models.DateTimeField(max_length=256, verbose_name='Date and time'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exam',
            name='exam_group',
            field=models.ForeignKey(verbose_name='Group', to='students.Group', max_length=256),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exam',
            name='subject',
            field=models.CharField(max_length=256, verbose_name='Subject Title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exam',
            name='teacher',
            field=models.CharField(max_length=256, verbose_name='Teacher'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='leader',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, verbose_name='Leader', to='students.Student'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='notes',
            field=models.TextField(verbose_name='Additional notes', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='date',
            field=models.DateField(verbose_name='Date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='present_day1',
            field=models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c \u21161'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='present_day10',
            field=models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c \u211610'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='present_day11',
            field=models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c \u211611'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='present_day12',
            field=models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c \u211612'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='present_day13',
            field=models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c \u211613'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='present_day14',
            field=models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c \u211614'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='present_day15',
            field=models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c \u211615'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='present_day16',
            field=models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c \u211616'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='present_day17',
            field=models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c \u211617'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='present_day18',
            field=models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c \u211618'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='present_day19',
            field=models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c \u211619'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='present_day2',
            field=models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c \u21162'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='present_day20',
            field=models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c \u211620'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='present_day21',
            field=models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c \u211621'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='present_day22',
            field=models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c \u211622'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='present_day23',
            field=models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c \u211623'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='present_day24',
            field=models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c \u211624'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='present_day25',
            field=models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c \u211625'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='present_day26',
            field=models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c \u211626'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='present_day27',
            field=models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c \u211627'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='present_day28',
            field=models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c \u211628'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='present_day29',
            field=models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c \u211629'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='present_day3',
            field=models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c \u21163'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='present_day30',
            field=models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c \u211630'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='present_day31',
            field=models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c \u211631'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='present_day4',
            field=models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c \u21164'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='present_day5',
            field=models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c \u21165'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='present_day6',
            field=models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c \u21166'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='present_day7',
            field=models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c \u21167'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='present_day8',
            field=models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c \u21168'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='present_day9',
            field=models.BooleanField(default=False, verbose_name='\u0414\u0435\u043d\u044c \u21169'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='student',
            field=models.ForeignKey(unique_for_month=b'date', verbose_name='Student', to='students.Student'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateField(null=True, verbose_name='Birthdate'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=256, verbose_name='Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=256, verbose_name='Last Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='middle_name',
            field=models.CharField(default=b'', max_length=256, verbose_name='Middle Name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='notes',
            field=models.TextField(verbose_name='Additional notes', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(upload_to=b'', null=True, verbose_name='Photo', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='student_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Group', to='students.Group', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='ticket',
            field=models.CharField(max_length=256, verbose_name='Ticket'),
            preserve_default=True,
        ),
    ]
