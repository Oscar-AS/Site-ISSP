import datetime
from django.db import models
from django.utils import timezone # Pour ajout méthode personnalisée
from django.contrib.auth.models import Group, Permission, User

# Create your models here.

class   Cours(models.Model):
    Type_document = models.CharField(max_length=100 , choices =[('option1','Cours') , ('option2','Exercices') , ('option3','Corrections')])
    Titre = models.CharField(max_length=200)
    Matiere_concerné = models.CharField(max_length=100)
    Niveau_concerné = models.CharField(max_length=100 , choices =[('option1','Licence 1') , ('option2','Licence 2') , ('option3','Licence 3'), ('option4','Master 1') , ('option5','Master 2') , ('option6','Master 3')])
    Description= models.TextField(max_length=2000)
    Support = models.FileField(upload_to= 'pdfs/' ) # Pour les pdf
    Auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    Date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Titre

class Sujet(models.Model):
    Type_test = models.CharField(max_length=100 , choices =[('option1','Sélection') , ('option2','Présélection') , ('option3','Résultats') ])
    Type_sujet = models.CharField(max_length=100 , choices =[('option1','Epreuve') , ('option2','Corrigé') ])
    Année = models.PositiveIntegerField()
    Niveau = models.CharField(max_length=100 , choices =[('Bac','Bac') , ('Licence','Licence') ])
    Support = models.FileField(upload_to= 'pdfs/' ) # Pour les pdf
    Auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    Date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Type_test

class Evenement(models.Model):
    Type_support=models.CharField(max_length=100 , choices =[('option1','Photos') , ('option2','Vidéos') ])
    Titre = models.TextField(max_length= 50, blank =True, null =True, default="Sans titre")
    Description= models.TextField( blank =True, null =True)
    Support = models.FileField(upload_to= 'media/' ) # Pour les pdf
    Auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    Date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Description

class Mots(models.Model):
    Nom =  models.CharField(max_length=100)
    Prénom =  models.CharField(max_length=100)
    Photo = models.ImageField(upload_to='media/')
    Fonction = models.CharField(max_length=100, default=" ")
    Mot =  models.CharField(max_length=3000)
    Date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Mot

class Fond(models.Model):
    Description= models.TextField()
    Support = models.FileField(upload_to='media/')
    Date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Description

class Statistique(models.Model):
    Nombre_fille= models.IntegerField()
    Nombre_garçon = models.IntegerField()
    Nombre_licence = models.IntegerField()
    Nombre_master = models.IntegerField()
    Nombre_professeur = models.IntegerField()
    Année_scolaire = models.CharField(max_length=10,default='')
    Date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Année_scolaire


class DemandePublicateur(models.Model):
    nom = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    sexe =models.CharField(max_length=10 , choices =[('H','Homme') , ('F','Femme') ])
    email = models.EmailField()
    raison = models.TextField()
    approuve = models.BooleanField(default=False)


class Membrepublicateur(models.Model):
    STATUS_CHOICES = (
        ('En attente', 'En attente'),
        ('Accepter', 'Accepter'),
        ('Rejetter', 'Rejetter'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nom  = models.CharField(max_length=100)
    prenom  = models.CharField(max_length=100)
    classe = models.CharField(max_length=100 , choices =[('Licence 1','Licence 1') , ('Licence 2','Licence 2') , ('Licence 3','Licence 3'), ('Master 1','Master 1') , ('Master 2','Master 2') , ('Master 3','Master 3')])
    sexe =models.CharField(max_length=10 , choices =[('H','Homme') , ('F','Femme') ])
    email = models.EmailField()
    numero = models.PositiveIntegerField()
    raison = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='En attente')
