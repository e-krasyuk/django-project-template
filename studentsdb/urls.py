from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView, TemplateView
from django.contrib.auth.decorators import login_required

from .settings import MEDIA_ROOT, DEBUG
from students.views.students import StudentUpdateView, StudentDeleteView, StudentCreateView
from students.views.contact_admin import ContactView
from students.views.groups import GroupDeleteView, GroupUpdateView, GroupCreateView, groups_list
from students.views.exams import ExamDeleteView, ExamUpdateView, ExamCreateView, exams_list
from students.views.journal import JournalView


js_info_dict = {
	'packages': ('students',),
}

urlpatterns = patterns('',
	# Students urls
	url(r'^$', 'students.views.students.students_list', name='home'),
	#url(r'^students/add/$', 'students.views.students.students_add', name='students_add'),
	url(r'^students/add/$', login_required(StudentCreateView.as_view()), name='students_add'),
	#url(r'^students/(?P<sid>\d+)/edit/$', 'students.views.students.students_edit', name='students_edit'),
	url(r'^students/(?P<pk>\d+)/edit/$', login_required(StudentUpdateView.as_view()), name='students_edit'),
	#url(r'^students/(?P<sid>\d+)/delete/$', 'students.views.students.students_delete', name='students_delete'),
	url(r'^students/(?P<pk>\d+)/delete/$', login_required(StudentDeleteView.as_view()), name='students_delete'),

	#Group urls
	url(r'^groups/$', login_required(groups_list), name='groups'),
	#url(r'^groups/add/$', 'students.views.groups.groups_add', name='groups_add'),
	url(r'^groups/add/$', login_required(GroupCreateView.as_view()), name='groups_add'),
	#url(r'^groups/(?P<gid>\d+)/edit/$', 'students.views.groups.groups_edit', name='groups_edit'),
	url(r'^groups/(?P<pk>\d+)/edit/$', login_required(GroupUpdateView.as_view()), name='groups_edit'),
	#url(r'^groups/(?P<gid>\d+)/delete/$', 'students.views.groups.groups_delete', name='groups_delete'),
	url(r'^groups/(?P<pk>\d+)/delete/$', login_required(GroupDeleteView.as_view()), name='groups_delete'),

	url(r'^journal/(?P<pk>\d+)?/?$', login_required(JournalView.as_view()), name='journal'),	

	url(r'^admin/', include(admin.site.urls)),

	#Exams urls
	url(r'^exams/$', login_required(exams_list), name='exams'),
	#url(r'^exams/add/$', 'students.views.exams.exams_add', name='exams_add'),
	url(r'^exams/add/$', login_required(ExamCreateView.as_view()), name='exams_add'),
	#url(r'^exams/(?P<eid>\d+)/edit/$', 'students.views.exams.exams_edit', name='exams_edit'),
	url(r'^exams/(?P<pk>\d+)/edit/$', login_required(ExamUpdateView.as_view()), name='exams_edit'),
	#url(r'^exams/(?P<eid>\d+)/delete/$', 'students.views.exams.exams_delete', name='exams_delete'),
	url(r'^exams/(?P<pk>\d+)/delete/$', login_required(ExamDeleteView.as_view()), name='exams_delete'),

	url(r'^admin/', include(admin.site.urls)),

	#Contact Admin Form
	url(r'^contact-admin/$', login_required(ContactView.as_view()), name='contact_admin'),

	#url for JS translation
	url(r'^jsi18n\.js$', 'django.views.i18n.javascript_catalog', js_info_dict),

	#i18n
	url('^set-language/$', 'students.views.set_language.set_language', name='set_language'),

	#User Related urls
	url(r'^users/profile/$', login_required(TemplateView.as_view(template_name='registration/profile.html')), name='profile'),
	url(r'^users/logout/$', auth_views.logout, kwargs={'next_page': 'home'},name='auth_logout'),
	url(r'^register/complete/$', RedirectView.as_view(pattern_name='home'),name='registration_complete'),
	url(r'^users/', include('registration.backends.simple.urls',namespace='users')),

	#Social Auth Related urls
	url('^social/', include('social.apps.django_app.urls', namespace='social')),
	)

if DEBUG:
	#serve files from media folder
	urlpatterns += patterns('', url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}))