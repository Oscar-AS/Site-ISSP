from django.contrib import admin

# Register your models here.

from .models import Cours, Evenement, Sujet

admin.site.register(Cours)
admin.site.register(Evenement)
admin.site.register(Sujet)

