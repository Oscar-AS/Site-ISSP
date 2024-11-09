from django.contrib import admin

# Register your models here.

from .models import Cours, Evenement, Sujet,Fond,Mots,Statistique, DemandePublicateur

admin.site.register(Cours)
admin.site.register(Evenement)
admin.site.register(Sujet)
admin.site.register(Fond)
admin.site.register(Mots)
admin.site.register(Statistique)
admin.site.register(DemandePublicateur)
