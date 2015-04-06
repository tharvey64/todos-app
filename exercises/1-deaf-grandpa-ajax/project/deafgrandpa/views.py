from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse

class GrandpaView(View):
	template = 'deafgrandpa/index.html'
	def get(self, request):
		return render(request, self.template)

	def post(self, request):
		pass