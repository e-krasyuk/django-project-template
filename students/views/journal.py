# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse



#Views for Journal
def journal(request):
	return render(request, 'students/journal.html')