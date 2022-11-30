from django.contrib import admin

from .models import (
    Feedbacks,
    Epis,
    Benefits,
    Scholarity,
    Dependents,
    Roles,
    Departments,
    People,
    Trainings,
    Employee
)


admin.site.register(Feedbacks)
admin.site.register(Epis)
admin.site.register(Benefits)
admin.site.register(Scholarity)
admin.site.register(Dependents)
admin.site.register(Roles)
admin.site.register(Departments)
admin.site.register(People)
admin.site.register(Trainings)
admin.site.register(Employee)