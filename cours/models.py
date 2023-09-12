import datetime
from django.db import models
from django.utils import timezone # Pour ajout méthode personnalisée


# Create your models here.

class   Cours(models.Model):
    Type_document = models.CharField(max_length=100 , choices =[('option1','Cours') , ('option2','Exercices') , ('option3','Corrections')])
    Titre = models.CharField(max_length=200)
    Matiere_concerné = models.CharField(max_length=100)
    Niveau_concerné = models.CharField(max_length=100 , choices =[('option1','Première année LPAS') , ('option2','Deuxième année LPAS') , ('option3','Troisième année LPAS')])
    Description= models.TextField()
    Support = models.FileField(upload_to= 'pdfs/' ) # Pour les pdf
    Auteur =  models.CharField(max_length=100, default="")
    Classe_auteur = models.CharField(max_length=100)
    Date_creation = models.DateTimeField(auto_now_add=True)
    Date_actualisation = models.DateTimeField(auto_now =True)
    Consultation = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.Titre

class Sujet(models.Model):
    Type_test = models.CharField(max_length=100 , choices =[('option1','Sélection') , ('option2','Présélection') ])
    Type_sujet = models.CharField(max_length=100 , choices =[('option1','Epreuve') , ('option2','Corrigé') ])
    Année = models.PositiveIntegerField()
    Support = models.FileField(upload_to= 'pdfs/' ) # Pour les pdf
    Auteur =  models.CharField(max_length=100)
    Classe_auteur = models.CharField(max_length=100, default=" ")
    Date_creation = models.DateTimeField(auto_now_add=True)
    Date_actualisation = models.DateTimeField(auto_now =True)
    Consultation = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.Type_test

class Evenement(models.Model):
    Description= models.TextField()
    Support = models.FileField(upload_to= 'media/' ) # Pour les pdf
    Auteur =  models.CharField(max_length=100)
    Classe_auteur = models.CharField(max_length=100, default=" ")
    Date_creation = models.DateTimeField(auto_now_add=True)
    Date_actualisation = models.DateTimeField(auto_now =True)
    Consultation = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.Description


class Message (models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=200)
    message = models.CharField(max_length = 1000)
    date_envoi = models.DateTimeField(auto_now_add=True)
