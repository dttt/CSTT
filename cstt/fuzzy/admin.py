from django.contrib import admin

from .models import Domain, FuzzySet, Parameter, FuzzyRule

# Register your models here.
admin.site.register(Domain)
admin.site.register(FuzzySet)
admin.site.register(Parameter)
admin.site.register(FuzzyRule)
