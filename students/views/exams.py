# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DeleteView, UpdateView, CreateView
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.forms import ModelForm, ValidationError

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

from ..models import Exam

#Views for Students

def exams_list(request):
	exams = Exam.objects.all()
	#try to order exams list
	order_by = request.GET.get('order_by', '')
	if order_by in ('subject', 'exam_group'):
		exams = exams.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			exams = exams.reverse()

	#paginate exams
	paginator = Paginator(exams, 2)
	page = request.GET.get('page')
	try:
		exams = paginator.page(page)
	except PageNotAnInteger:
		# If page not an integer, deliver first page
		exams = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		exams = paginator.page(paginator.num_pages)

	return render(request, 'students/exams_list.html', 
		{'exams': exams})

#def exams_add(request):
	#return HttpResponse('<h1>Exam Add Form</h1>')

class ExamCreateForm(ModelForm):
	class Meta:
		model = Exam
		fields ='__all__'
		#exclude = ("",)

	def __init__(self, *args, **kwargs):
		super(ExamCreateForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper(self)

		#set form tag attributes
		#set form tag attributes
		self.helper.form_action = reverse('exams_add')
		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'
		self.helper.attrs = {'novalidate': ''} #off browser validation, when click cancel_button

		#set form field properties
		self.helper.help_text_inline = True
		self.helper.html5_required = True
		self.helper.label_class = 'col-sm-2 control-label'
		self.helper.field_class = 'col-sm-10'

		#add buttons
		self.helper.layout.append(FormActions(
			Submit('add_button', u'Зберегти', css_class="btn btn-primary"),
			Submit('cancel_button', u'Скасувати', css_class="btn btn-link"),
		))

class ExamCreateView(CreateView):
	model = Exam
	template_name = 'students/exams_add.html'
	form_class = ExamCreateForm

	def get_success_url(self):
		#return u'%s?status_message=Студента успішно створено!' % reverse('home')
		messages.success(self.request, u'Іспит створено!')
		return reverse('exams')

	def post(self, request, *args, **kwargs):
		if request.POST.get('cancel_button'):
			#return HttpResponseRedirect(u'%s?status_message=Створення відмінено!' % reverse('home'))
			messages.info(self.request, u'Створення відмінено!')
			return HttpResponseRedirect(reverse('exams'))
		else:
			#Use post method from UpdateView
			return super(ExamCreateView, self).post(request, *args, **kwargs)

#def exams_edit(request, eid):
	#return HttpResponse('<h1>Edit Exam %s</h1>' % eid)

class ExamUpdateForm(ModelForm):
	class Meta:
		model = Exam
		fields ='__all__'

	def __init__(self, *args, **kwargs):
		super(ExamUpdateForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper(self)

		# set form tag attributes
		self.helper.form_action = reverse('exams_edit', kwargs={'pk': kwargs['instance'].id})
		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'

		# set form field properties
		self.helper.help_text_inline = True
		self.helper.html5_required = True
		self.helper.label_class = 'col-sm-2 control-label'
		self.helper.field_class = 'col-sm-10'

		# add buttons
		self.helper.layout.append(FormActions(
			Submit('add_button', u'Зберегти', css_class="btn btn-primary"),
			Submit('cancel_button', u'Скасувати', css_class="btn btn-link"),
		))

class ExamUpdateView(UpdateView):
	model = Exam
	template_name = 'students/exams_edit.html'
	form_class = ExamUpdateForm

	def get_success_url(self):
		#return u'%s?status_message=Студента успішно збережено!' % reverse('home')
		messages.success(self.request, u'Іспит відредаговано!')
		return reverse('exams')

	def post(self, request, *args, **kwargs):
		if request.POST.get('cancel_button'):
			messages.info(self.request, u'Редагування відмінено!')
			return HttpResponseRedirect(reverse('exams'))
				#u'%s?status_message=Редагування відмінено!' % reverse('home'))
		else:
			return super(ExamUpdateView, self).post(request, *args, **kwargs)

#def exams_delete(request, eid):
	#return HttpResponse('<h1>Delete Exam %s</h1>' % eid)

class ExamDeleteView(DeleteView):
	model = Exam
	template_name = 'students/exams_confirm_delete.html'

	def get_success_url(self):
		return reverse('exams')

	def delete(self, request, *args, **kwargs):
		exam = self.get_object()
		exam.delete()
		messages.success(self.request, u'Іспит видалено!')
		return HttpResponseRedirect(self.get_success_url())