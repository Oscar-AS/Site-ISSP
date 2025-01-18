from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 
from django.urls import include, path
from cours.views import  evenement_create,ajout,sujet_create,cours_create,manage_requests,accept_request, reject_request,Membre_publicateur, index,contact,connexion, register,home,index_evenement,index_cours,index_sujet,index_information,index_information_site,formulaire_message




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("cours.urls")),

    ##### CONNEXION  ###############

    path('login', connexion, name="connexion"),
    path('register', register, name="register"),

    path("Accueil/",index, name="index"),
    path("cours/",index_cours, name="index_cours"),
    path('cours/<str:page_name>/', index_cours, name='index_cours'),
    


    path('contact/', contact, name='contact'),

    path("evenement/",index_evenement, name="index_evenement"),
     path('evenement/<str:page_name>/', index_evenement, name='index_evenement'),
    
    #path("cours/<str:fichier>",telechargé, name="telechargé"),
    path("sujet/",index_sujet, name="index_sujet"),
    path('sujet/<str:page_name>/', index_sujet, name='index_sujet'),
    path("information/",index_information, name="index_information"),
    path("information/site",index_information_site, name="index_information_site"),


    path('message/',formulaire_message, name='formulaire_message'),


## Chemin pour la création d'un compte utilisateur




    path('membership_request/', Membre_publicateur, name='Membre_publicateur'),
    path('manage_requests/', manage_requests, name='manage_requests'),
    path('accept_request/<int:request_id>/', accept_request, name='accept_request'),
    path('reject_request/<int:request_id>/', reject_request, name='reject_request'),



################## Chemin pour gerer les formulaires d'ajout des elements


path('ajout/', ajout, name='ajout'),
path('ajout/cours/', cours_create, name='cours_create'),
path('ajout/sujet/', sujet_create, name='sujet_create'),
path('ajout/evenement/', evenement_create, name='evenement_create'),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)