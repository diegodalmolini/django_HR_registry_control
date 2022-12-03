from django.urls import path

from .views import HomeView, EmployeeListView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('funcionarios', EmployeeListView.as_view(), name='funcionarios')

]