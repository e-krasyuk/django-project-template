from datetime import datetime

from django.http import HttpResponse

from settings import DEBUG

from bs4 import BeautifulSoup

class RequestTimeMiddleware(object):
	''' Display request time on a page '''

	def process_request(self, request):
		request.start_time = datetime.now()
		return None

	def process_response(self, request, response):
		#if our process_request was canceled somwhere within
		#middleware stack, we can not calculate time
		if not hasattr(request, 'start_time'):
			return response

		#calculate request execution time
		request.end_time = datetime.now()
		time_delta = request.end_time - request.start_time
		if DEBUG == True and 'text/html' in response.get('Content-Type', ''):
			soup = BeautifulSoup(response.content, 'lxml')
        	# response.content may be empty in case of HttpResponseRedirct object
        	if soup.body:
				time_measure_tag = soup.new_tag('code', style='margin-left:20px')
				time_measure_tag.append('Request took: %s' % str(time_delta))
				soup.body.insert(0, time_measure_tag)
				response.content = soup.prettify(soup.original_encoding)
			
        	return response

			#response.write('<br>Request time: %s' % str(
				#request.end_time - request.start_time))
		#return response

	def process_view(self, request, view, args, kwargs):
		return None

	def process_template_response(self, request, response):
		return response

	def process_exception(self, request, exception):
		return HttpResponse('Exception found: %s' % exception)


