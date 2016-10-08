from django.conf.urls import patterns, include, url
from django.contrib import admin
from .settings import MEDIA_ROOT, DEBUG
from students.views.students import StudentUpdateView, StudentDeleteView

urlpatterns = patterns('',
	# Students urls
	url(r'^$', 'students.views.students.students_list', name='home'),
	url(r'^students/add/$', 'students.views.students.students_add', name='students_add'),
	#url(r'^students/(?P<sid>\d+)/edit/$', 'students.views.students.students_edit', name='students_edit'),
	url(r'^students/(?P<pk>\d+)/edit/$', StudentUpdateView.as_view(), name='students_edit'),
	#url(r'^students/(?P<sid>\d+)/delete/$', 'students.views.students.students_delete', name='students_delete'),
	url(r'^students/(?P<pk>\d+)/delete/$', StudentDeleteView.as_view(), name='students_delete'),

	#Group urls
	url(r'^groups/$', 'students.views.groups.groups_list', name='groups'),
	url(r'^groups/add/$', 'students.views.groups.groups_add', name='groups_add'),
	url(r'^groups/(?P<gid>\d+)/edit/$', 'students.views.groups.groups_edit', name='groups_edit'),
	url(r'^groups/(?P<gid>\d+)/delete/$', 'students.views.groups.groups_delete', name='groups_delete'),

	url(r'^journal/$', 'students.views.journal.journal', name='journal'),	

	url(r'^admin/', include(admin.site.urls)),

	#Exams urls
	url(r'^exams/$', 'students.views.exams.exams_list', name='exams'),
	url(r'^exams/add/$', 'students.views.exams.exams_add', name='exams_add'),
	url(r'^exams/(?P<eid>\d+)/edit/$', 'students.views.exams.exams_edit', name='exams_edit'),
	url(r'^exams/(?P<eid>\d+)/delete/$', 'students.views.exams.exams_delete', name='exams_delete'),

	url(r'^journal/$', 'students.views.journal.journal', name='journal'),	

	url(r'^admin/', include(admin.site.urls)),

	#Contact Admin Form
	url(r'^contact-admin/$', 'students.views.contact_admin.contact_admin', name='contact_admin'),
	)

if DEBUG:
	#serve files from media folder
	urlpatterns += patterns('', url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}))