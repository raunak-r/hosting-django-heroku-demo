from django.http import HttpResponse
from django.views import View

class HomePageView(View):
	def get(self, request):
		return HttpResponse('Wow! If you\'re seeing this page on internet then grab yourself a beer')
