from django.urls import path

from .views import HomeView, EmployeeListView, EmployeeDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),

    path('funcionarios', EmployeeListView.as_view(), name='funcionarios'),

    path('funcionario/<int:pk>', EmployeeDetailView.as_view(), name='funcionario')

]