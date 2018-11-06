from django.shortcuts import render
from  django.views.generic import View
from  django.http import  HttpResponse
from django.views.generic import View,TemplateView,DetailView,ListView
from . import models


# Create your views here. function base view
# def index(request):
#     return render(request,'index.html')


# Create your views here. class base view without template base
# class CBView(View):
#     def get(self,request):
#         return HttpResponse("THIS IS CLASS BASED VIEW")

# Create your views here. class base view with template base
# class IndexView(TemplateView):
#     template_name = 'index.html'
#
#     def get_context_data(self, **kwargs):
#         contaxt = super().get_context_data(**kwargs)
#         contaxt ['injectme'] = 'BASIC INJECTION'
#         return contaxt

# ACRUAL CLASS BASE VIEW TESTING BY USING MODELS

class SchoolListView(ListView):
    model = models.School


class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'basic_app/school_detail.html'
