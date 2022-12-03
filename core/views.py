from django.views.generic import TemplateView, ListView, DetailView
from .models import Employee

class HomeView(TemplateView):
    template_name = 'home.html'


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee-list.html'


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee-detail.html'
