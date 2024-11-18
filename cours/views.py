
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
from django.contrib.auth.models import User
from django.http import FileResponse,HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render , get_object_or_404, redirect
from .models import Cours, Evenement, Sujet, Mots, Fond, Statistique

from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView
from .forms import DemandePublicateurForm, UserForm, ContactForm, CoursForm

from io import BytesIO
import base64
from django.core.mail import send_mail
from django.db.models import Q
# import os
from . import views

########################################################## COURS######################################

## Ce code permet d'afficher la page d'acceuil principale

@login_required
def index(request):
  liste_mot_dir =Mots.objects.filter(Q(Fonction__icontains= "directeur")).order_by('-Date')[:1]

  liste_mot= Mots.objects.exclude(Q(Fonction__icontains= "directeur")).order_by('-Date')[:3]

  liste_fond= Fond.objects.order_by('-Date')[:3]

  liste_stat = Statistique.objects.order_by('-Date')[:1]

  nbr_fille = liste_stat[0].Nombre_fille
  nbr_garçon = liste_stat[0].Nombre_garçon
  nbr_licence = liste_stat[0].Nombre_licence
  nbr_master = liste_stat[0].Nombre_master
  nbr_prof = liste_stat[0].Nombre_professeur

  context ={"liste_mot": liste_mot, "liste_mot_dir": liste_mot_dir, "liste_fond": liste_fond, "nbr_fille":nbr_fille, "nbr_garçon":nbr_garçon, "nbr_licence":nbr_licence, "nbr_master":nbr_master, "nbr_prof": nbr_prof}

  return render (request, "Acceuil1.html",context)

def home(request):
  return render (request, "Home.html")

## Ce code permet d'afficher la page d'acceuil  des cours

@login_required
def index_cours(request):
       niveaux = Cours.objects.values_list('Niveau_concerné', flat=True).distinct()
       cours_list = Cours.objects.all().order_by('-Date_creation')

       item_name=request.GET.get('item_nom')
       if item_name!='' and item_name is not None:
        niveaux = Cours.objects.values_list('Niveau_concerné', flat=True).distinct()
        cours_list =Cours.objects.filter(Q(Description__icontains=item_name) | Q(Titre__icontains=item_name) | Q(Matiere_concerné__icontains=item_name) ).order_by('-Date_creation')
       else:
        niveaux = Cours.objects.values_list('Niveau_concerné', flat=True).distinct()
        cours_list = Cours.objects.all().order_by('-Date_creation')
       return render(request, 'Acceuil2.html', {'niveaux': niveaux ,'cours_list':cours_list})








########################################################  EVENEMENT ############################################################


## Ce code permet de lister tous les évènements qui ont été publié.
@login_required
def index_evenement(request):
   item_name=request.GET.get('item_nom')
   if item_name!='' and item_name is not None:
      liste_photos= Evenement.objects.filter(Q(Type_support="option1") & Q(Description__icontains=item_name)).order_by('-Date_creation')
      liste_videos= Evenement.objects.filter(Q(Type_support="option2") & Q(Description__icontains=item_name)).order_by('-Date_creation')

   else:

      liste_photos= Evenement.objects.filter(Type_support="option1").order_by('-Date_creation')
      liste_videos= Evenement.objects.filter(Type_support="option2").order_by('-Date_creation')
   context ={"liste_photos": liste_photos, "liste_videos": liste_videos}
   return render (request, "Evenement.html", context)





####################################################  SUJET ##################################################
@login_required
def index_sujet(request):


  item_name=request.GET.get('item_nom')
  if item_name!='' and item_name is not None:

    liste_sujet_sel = Sujet.objects.filter(Q(Type_test= 'option1') & Q(Type_sujet= 'option1') & Q( Année__icontains=item_name)).order_by('-Date_creation')
    liste_sujet_pres = Sujet.objects.filter(Q(Type_test= 'option2') & Q(Type_sujet= 'option1') & Q( Année__icontains=item_name)).order_by('-Date_creation')
    liste_sujet_res = Sujet.objects.filter(Q(Type_test= 'option3') & Q( Année__icontains=item_name)).order_by('-Date_creation')

    liste_sujet_sel_cor = Sujet.objects.filter(Q(Type_test= 'option1') & Q(Type_sujet= 'option2') & Q( Année__icontains=item_name)).order_by('-Date_creation')
    liste_sujet_pres_cor = Sujet.objects.filter(Q(Type_test= 'option2') & Q(Type_sujet= 'option2') & Q( Année__icontains=item_name)).order_by('-Date_creation')

  else:
    liste_sujet_sel = Sujet.objects.filter(Type_test= 'option1' , Type_sujet= 'option1').order_by('-Date_creation')
    liste_sujet_pres = Sujet.objects.filter(Type_test= 'option2' , Type_sujet= 'option1').order_by('-Date_creation')
    liste_sujet_res = Sujet.objects.filter(Type_test= 'option3').order_by('-Date_creation')

    liste_sujet_sel_cor = Sujet.objects.filter(Type_test= 'option1' , Type_sujet= 'option2').order_by('-Date_creation')
    liste_sujet_pres_cor = Sujet.objects.filter(Type_test= 'option2' , Type_sujet= 'option2').order_by('-Date_creation')

  context={"liste_sujet_sel": liste_sujet_sel , "liste_sujet_pres" : liste_sujet_pres , "liste_sujet_res" : liste_sujet_res , "liste_sujet_sel_cor": liste_sujet_sel_cor , "liste_sujet_pres_cor" : liste_sujet_pres_cor}

  return render (request, "Sujet.html" , context)

@login_required
def index_sujet_sel(request):
  liste_sujet_sel = Sujet.objects.filter(Type_test= 'option1')
  context={"liste_sujet_sel": liste_sujet_sel}
  return render (request,"Sujet_selection.html",context)

@login_required
def index_sujet_pres(request):
  liste_sujet_pres = Sujet.objects.filter(Type_test= 'option2')
  context={"liste_sujet_pres" : liste_sujet_pres}
  return render (request,"Sujet_preselection.html",context)

@login_required
def index_sujet_pres(request):
  liste_sujet_pres = Sujet.objects.filter(Type_test= 'option2')
  context={"liste_sujet_pres" : liste_sujet_pres}
  return render (request,"Sujet_preselection.html",context)



################################################### INFORMATION ########################################
@login_required
def index_information(request):
  return render (request, "Information.html")


@login_required
def index_information_fil(request):
  return render (request, "Information_filiere.html")


@login_required
def index_information_site(request):
  return render (request, "Information_site.html")


################################################### Formulaire message #######################"

@login_required
def contact(request):
       if request.method == 'POST':
           form = ContactForm(request.POST)
           if form.is_valid():
               nom = form.cleaned_data['nom']
               prenom = form.cleaned_data['prenom']
               numero = form.cleaned_data['numero']
               email = form.cleaned_data['email']
               message = form.cleaned_data['message']

               destinataire = 'kafjudicaeloscar@gmail.com'  # Remplacez ceci par votre e-mail de réception
               sujet = f"Nouveau message de {nom} {prenom}"
               contenu = f"Nom: {nom}\nPrenom: {prenom}\nNumero: {numero}\nEmail: {email}\n\nMessage:\n{message}"

               send_mail(sujet, contenu, email, [destinataire])
               return render(request, 'confirmation.html')  # Créez un template pour la confirmation
       else:
           form = ContactForm()
       return render(request, 'contact.html', {'form': form})  # Créez un template pour le formulaire de contact




@login_required
def formulaire_message(request):
    if request.method == 'POST':
        email = request.POST['email']
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        numero = request.POST['phone']
        message = request.POST['message']

        destinataire = 'projetsiteweblpas@gmail.com'
        sujet = f"Nouveau message de {nom} {prenom}"
        contenu = f"Nom: {nom}\nPrénom: {prenom}\nNuméro: {numero}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            send_mail(sujet, contenu, email, [destinataire])
            return render(request, 'confirmation.html', {'nom': nom})
        except Exception as e:
            # Redirection vers un template d'échec
            return render(request, 'error.html', {'error_message': str(e)})
    return render(request, 'message.html')







########################################## CREATION DU COMPTE ####################################


def connexion(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            # Ajoutez un message d'erreur qui sera affiché dans la page actuelle
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")

    return render(request, "login.html")



def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            if User.objects.filter(username=username).exists():
                messages.error(request, "Le nom d'utilisateur existe déjà. Veuillez en choisir un autre.")
            else:
                user = form.save(commit=False)
                password = form.cleaned_data.get('password1')
                user.set_password(password)
                user.save()

                email = form.cleaned_data.get('email')
                nom = form.cleaned_data.get('nom')
                prenom = form.cleaned_data.get('prenom')

                sujet = "Confirmation de création de compte"
                contenu = (
                    f"Bonjour {prenom} {nom},\n\n"
                    "Votre compte a été créé avec succès. Vous pouvez maintenant vous connecter avec vos identifiants.\n\n"
                    f"Nom d'utilisateur : {username}\n"
                    f"Mot de passe : {password}\n\n"
                    "Merci de garder ces informations confidentielles."
                )
                send_mail(sujet, contenu, "projetsiteweblpas@gmail.com", [email])

                messages.success(request, "Compte créé avec succès. Un email de confirmation a été envoyé.")
                return redirect('connexion')
    else:
        form = UserForm()

    return render(request, "register.html", {"form": form})

########################################################################################### DEMANDE PUBLICATEUR################################""

from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group, Permission
from .models import Membrepublicateur
from .forms import MembrepublicateurForm

@login_required
def Membre_publicateur(request):

     # Vérification si l'utilisateur fait déjà partie des publicateurs
    if Membrepublicateur.objects.filter(user=request.user).exists():
        messages.info(request, "Vous êtes déjà membre du groupe des publicateurs.")
        return redirect('index')

## Si l'utilisateur ne fait pas partie des publicateurs

    if request.method == 'POST':

        form = MembrepublicateurForm(request.POST)
        if form.is_valid():
            Membre_publicateur = form.save(commit=False)
            Membre_publicateur.status = 'En attente'
            Membre_publicateur.user = request.user
            Membre_publicateur.save()
####################################### Mail de validation

            email = Membre_publicateur.email
            nom = Membre_publicateur.nom
            prenom = Membre_publicateur.prenom

            destinataire = email  # Remplacez ceci par votre e-mail de réception
            sujet = f"Nouveau message de projetsiteweblpas@gmail.com"
            contenu = f"Monsieur/Madame {nom} {prenom},\n \n Nous accusons réception de votre demande d'adhésion au groupe des publicateurs. \n Votre demande sera examiner et vous aurez une reponse dans un bref délai d'une semaine. \n Merci pour la confiance."

            send_mail(sujet, contenu, "projetsiteweblpas@gmail.com", [destinataire])

            sujet1 = f"Nouvelle demande"
            contenu1 = f"Monsieur/Madame {nom} {prenom}, vient de faire une demande d'adhésion au groupe des publicateurs.\n \n Merci de vérifier la page des demandes dans le site."

            send_mail(sujet1, contenu1, "projetsiteweblpas@gmail.com", ["projetsiteweblpas@gmail.com"])


            messages.success(request, "Votre demande a été soumise avec succès.")
            return redirect('index')
    else:
        form = MembrepublicateurForm()
    return render(request, 'membre_publicateur.html', {'form': form})

@login_required
def manage_requests(request):
    if request.user.is_superuser:

        requests = Membrepublicateur.objects.filter(status='En attente')
        if not requests:
           return render(request, 'Pas_demande.html', {'requests': requests})
        else:
           return render(request, 'manage_requests.html', {'requests': requests})

    else:
        messages.info(request, "Vous n'êtes pas accesible à cette page")
        return redirect('index')

@login_required
def accept_request(request, request_id):
      if request.user.is_superuser:
        Membre_publicateur = Membrepublicateur.objects.get(id=request_id)
        Membre_publicateur.status = 'Accepter'

        Membre_publicateur.save()
        group = Group.objects.get(name='publicateur')
        Membre_publicateur.user.groups.add(group)


        email = Membre_publicateur.email
        nom = Membre_publicateur.nom
        prenom = Membre_publicateur.prenom

        destinataire = email  # Remplacez ceci par votre e-mail de réception
        sujet = f"Nouveau message de projetsiteweblpas@gmail.com"
        contenu = f"Monsieur/Madame {nom} {prenom},\n \n Nous vous informons que votre demande d'adhésion au groupe des publicateurs a été accepté. \n Maintenant vous pouvez faire des publication sur le site en vous rendant sur l'onglet publier."

        send_mail(sujet, contenu, "projetsiteweblpas@gmail.com", [destinataire])

        return redirect('manage_requests')
      else:
        return redirect('index')

@login_required
def reject_request(request, request_id):
      if request.user.is_superuser:
        Membre_publicateur = Membrepublicateur.objects.get(id=request_id)
        Membre_publicateur.status = 'rejetter'
        Membre_publicateur.save()

        email = Membre_publicateur.email
        nom = Membre_publicateur.nom
        prenom = Membre_publicateur.prenom

        destinataire = email  # Remplacez ceci par votre e-mail de réception
        sujet = f"Nouveau message de projetsiteweblpas@gmail.com"
        contenu = f"Monsieur/Madame {nom} {prenom},\n \n Nous vous informons que votre demande d'adhésion au groupe des publicateurs n'a pas été accepté."

        send_mail(sujet, contenu, "projetsiteweblpas@gmail.com", [destinataire])

        return redirect('manage_requests')

      else:
        return redirect('index')



#################################### VUE POUR FORMULAIRE POUR L'AJOUT DES ELEMENTS ##################################


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CoursForm, SujetForm,EvenementForm


# Fonction de test pour vérifier si l'utilisateur est un admin ou un membre du staff
def is_admin_or_staff(user):
    return user.is_superuser or user.is_staff

from django.contrib.auth.decorators import user_passes_test
def admin_required(view_func):
    decorated_view_func = user_passes_test(lambda user: user.is_superuser, login_url='Accueil/')(view_func)
    return decorated_view_func

def staff_required(view_func):
    decorated_view_func = user_passes_test(lambda user: user.is_staff, login_url='Accueil/')(view_func)
    return decorated_view_func



@staff_required
def cours_create(request):
    if request.method == 'POST':
        form = CoursForm(request.POST, request.FILES)
        if form.is_valid():
            cours = form.save(commit=False)  # Crée une instance du modèle mais ne la sauvegarde pas encore
            cours.Auteur = request.user
            cours.save()
            messages.success(request, 'Cours ajouté avec succès.')
            return redirect('cours_create')  # Redirection pour réinitialiser le formulaire
        else:
            messages.error(request, 'Erreur lors de l\'ajout du cours.')
    else:
        form = CoursForm()

    return render(request, 'cours_ajout.html', {'form': form})


@staff_required
def sujet_create(request):
    if request.method == 'POST':
        form = SujetForm(request.POST, request.FILES)
        if form.is_valid():
            sujet = form.save(commit=False)  # Crée une instance du modèle mais ne la sauvegarde pas encore
            sujet.Auteur = request.user
            sujet.save()
            messages.success(request, 'Sujet ajouté avec succès.')
            return redirect('sujet_create')  # Redirection pour réinitialiser le formulaire
        else:
            messages.error(request, 'Erreur lors de l\'ajout du sujet.')
    else:
        form = SujetForm()

    return render(request, 'cours_ajout.html', {'form': form})



@staff_required
def evenement_create(request):
    if request.method == 'POST':
        form = EvenementForm(request.POST, request.FILES)
        if form.is_valid():
            evenement = form.save(commit=False)  # Crée une instance du modèle mais ne la sauvegarde pas encore
            evenement.Auteur = request.user
            evenement.save()
            messages.success(request, 'Evènement ajouté avec succès.')
            return redirect('evenement_create')  # Redirection pour réinitialiser le formulaire
        else:
            messages.error(request, 'Erreur lors de l\'ajout de l\'évènement.')
    else:
        form = EvenementForm()

    return render(request, 'cours_ajout.html', {'form': form})


@staff_required
def ajout(request):

  return render (request, "ajout.html")

