# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DeleteView
from django.core.urlresolvers import reverse
from django.contrib import messages

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

def groups_add(request):
	return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' % gid)

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