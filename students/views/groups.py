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

from ..models import Group, Student

#Views for Groups

def groups_list(request):
	groups = Group.objects.all()
	#try to order groups list
	order_by = request.GET.get('order_by', '')
	if order_by in ('title','leader'):
		groups = groups.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			groups = groups.reverse()

	#paginate groups
	paginator = Paginator(groups, 2)
	page = request.GET.get('page')
	try:
		groups = paginator.page(page)
	except PageNotAnInteger:
		# If page not an integer, deliver first page
		groups = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		groups = paginator.page(paginator.num_pages)
		
	return render(request, 'students/groups_list.html', 
		{'groups': groups})

#def groups_add(request):
	#return HttpResponse('<h1>Group Add Form</h1>')

class GroupCreateForm(ModelForm):
	class Meta:
		model = Group
		fields ='__all__'
		#exclude = ("",)

	def __init__(self, *args, **kwargs):
		super(GroupCreateForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper(self)

		#set form tag attributes
		#set form tag attributes
		self.helper.form_action = reverse('groups_add')
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

class GroupCreateView(CreateView):
	model = Group
	template_name = 'students/groups_add.html'
	form_class = GroupCreateForm

	def get_success_url(self):
		#return u'%s?status_message=Студента успішно створено!' % reverse('home')
		messages.success(self.request, u'Групу створено!')
		return reverse('groups')

	def post(self, request, *args, **kwargs):
		if request.POST.get('cancel_button'):
			#return HttpResponseRedirect(u'%s?status_message=Створення відмінено!' % reverse('home'))
			messages.info(self.request, u'Створення відмінено!')
			return HttpResponseRedirect(reverse('groups'))
		else:
			#Use post method from UpdateView
			return super(GroupCreateView, self).post(request, *args, **kwargs)

#def groups_edit(request, gid):
	#return HttpResponse('<h1>Edit Group %s</h1>' % gid)

class GroupUpdateForm(ModelForm):
	class Meta:
		model = Group

	def __init__(self, *args, **kwargs):
		super(GroupUpdateForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper(self)

		# set form tag attributes
		self.helper.form_action = reverse('groups_edit', kwargs={'pk': kwargs['instance'].id})
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
	
	def clean_leader(self):
		students = Student.objects.filter(student_group=self.instance)
		if self.cleaned_data['leader'] not in students:
			raise ValidationError(u'Студент має належити до цієї групи', code="invalid")

		return self.cleaned_data['leader']
	

class GroupUpdateView(UpdateView):
	model = Group
	template_name = 'students/groups_edit.html'
	form_class = GroupUpdateForm

	def get_success_url(self):
		#return u'%s?status_message=Студента успішно збережено!' % reverse('home')
		messages.success(self.request, u'Групу відредаговано!')
		return reverse('groups')

	def post(self, request, *args, **kwargs):
		if request.POST.get('cancel_button'):
			messages.info(self.request, u'Редагування відмінено!')
			return HttpResponseRedirect(reverse('groups'))
				#u'%s?status_message=Редагування групи відмінено!' % reverse('home'))
		else:
			return super(GroupUpdateView, self).post(request, *args, **kwargs)

#def groups_delete(request, gid):
	#return HttpResponse('<h1>Delete Group %s</h1>' % gid)

class GroupDeleteView(DeleteView):
	model = Group
	template_name = 'students/groups_confirm_delete.html'

	def get_success_url(self):
		return reverse('home')

	def delete(self, request, *args, **kwargs):
		group = self.get_object()
		if group.student_set.exists():
			messages.error(self.request, u'Група %s не порожня!' % group.title)
		else:
			group.delete()
			messages.success(self.request, u'Групу видалено!')
		return HttpResponseRedirect(self.get_success_url())