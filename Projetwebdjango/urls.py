

from django.contrib import admin
from django.urls import include, path
from cours.views import  index_evenement,index_cours,index_cours_L1,index_cours_L2,index_cours_L3,index_sujet,index_sujet_pres,index_sujet_sel,index_information,index_information_fil,index_information_site,formulaire_message


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("cours.urls")),
    path("cours/",index_cours, name="index_cours"),
    path("evenement/",index_evenement, name="index_evenement"),


    path("cours/cours_L1/",index_cours_L1, name="index_cours_L1"),
    #path("cours/cours_L1/recherche",Cours_recherche_L1, name="Cours_recherche_L1"),


    path("cours/cours_L2/",index_cours_L2, name="index_cours_L2"),
    path("cours/cours_L3/",index_cours_L3, name="index_cours_L3"),
    
    
    path("sujet/",index_sujet, name="index_sujet"),
    path("sujet/selection/",index_sujet_sel, name="index_sujet_sel"),
    
    path("sujet/preselection/",index_sujet_pres, name="index_sujet_pres"),
    path("information/",index_information, name="index_information"),
    path("information/filière",index_information_fil, name="index_information_fil"),
    path("information/site",index_information_site, name="index_information_site"),
    path('message/',formulaire_message, name='formulaire_message'),

    #path("cours/cours_L1/recherche",Cours_recherche_Form, name='Cours_recherche_Form'),


]


           



