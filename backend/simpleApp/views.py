from django.http import HttpResponse
from django.views import View

import logging
logger = logging.getLogger(__name__)

class HomePageView(View):
	def get(self, request):
		logger.info('Inside Home Page')
		return HttpResponse('Wow! If you\'re seeing this page on internet then grab yourself a beer')
