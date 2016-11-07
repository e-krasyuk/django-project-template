from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy, reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.views.generic.edit import FormView
from django.utils.translation import ugettext as _
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required

from studentsdb.settings import ADMIN_EMAIL

from django.contrib import messages

import logging

class ContactForm(forms.Form):
	from_email = forms.EmailField(
		label=_(u'Your email'))

	subject = forms.CharField(
		label=_(u'Message header'),
		max_length=128)

	message = forms.CharField(
		label=_(u'Message text'),
		max_length=2560,
		widget=forms.Textarea)

	def __init__(self, *args, **kwargs):
		#call original initializator
		super(ContactForm, self).__init__(*args, **kwargs)

		#this helper object allows us to customize form
		self.helper = FormHelper()

		#form tags attributes
		self.helper.form_class = 'form-horizontal'
		self.helper.form_method = 'post'
		self.helper.form_action = reverse('contact_admin')

		#twitter bootstrap styles
		self.helper.help_text_inline = True
		self.helper.html5_required = True
		self.helper.label_class = 'col-sm-2 control-label'
		self.helper.field_class = 'col-sm-10'

		#form buttons
		self.helper.add_input(Submit('send_button', _(u'Send'))) 

	from_email = forms.EmailField(
		label=_(u'Your email'))

	subject = forms.CharField(
		label=_(u'Message header'),
		max_length=128)

	message = forms.CharField(
		label=_(u'Message text'),
		max_length=2560,
		widget=forms.Textarea)

class ContactView(FormView):
	template_name = 'contact_admin/form.html'
	form_class = ContactForm
	success_url = reverse_lazy('contact_admin')

	def form_valid(self, form):
		subject = form.cleaned_data['subject']
		message = form.cleaned_data['message']
		from_email = form.cleaned_data['from_email']

		try:
			send_mail(subject, message, from_email, [ADMIN_EMAIL])
		except Exception:
			messages.error(self.request, _(u"While sending email erro occurred. Try to use the form later."))
			logger = logging.getLogger(__name__)
			logger.exception(message)
		else:
			messages.success(self.request, _(u"Message successfully sent!"))
		return super(ContactView, self).form_valid(form)

	@method_decorator(permission_required('auth.add_user'))
	def dispatch(self, *args, **kwargs):
		return super(ContactView, self).dispatch(*args, **kwargs)



