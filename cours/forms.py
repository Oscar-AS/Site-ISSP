from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

from .models import DemandePublicateur,Cours,Sujet,Evenement

class ContactForm(forms.Form):
       nom = forms.CharField(max_length=100)
       prenom = forms.CharField(max_length=100)
       numero = forms.IntegerField()
       email = forms.EmailField()
       message = forms.CharField(widget=forms.Textarea)



class DemandePublicateurForm(forms.ModelForm):
    class Meta:
        model = DemandePublicateur
        fields = ['nom', 'profession', 'sexe','email', 'raison']




from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    nom = forms.CharField(max_length=100)
    prenom = forms.CharField(max_length=100)
    email = forms.EmailField()
    filière = forms.ChoiceField(choices=[
        ('option1', 'Licence professionnelle en Analyse statistique'),
        ('option2', 'Master professionnelle en Statistique économie')
    ])
    classe = forms.ChoiceField(choices=[
        ('option1', 'Première année'),
        ('option2', 'Deuxième année'),
        ('option3', 'Troisième année')
    ])

    class Meta:
        model = User
        fields = ['nom', 'prenom', 'username', 'email', 'filière', 'classe', 'password1', 'password2']
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None
        }

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.nom = self.cleaned_data['nom']
        user.username = self.cleaned_data['username']
        user.prenom = self.cleaned_data['prenom']
        user.filière = self.cleaned_data['filière']
        user.classe = self.cleaned_data['classe']

        if commit:
            user.save()
        return user


########################################################################################################""

from django import forms
from .models import Membrepublicateur

class MembrepublicateurForm(forms.ModelForm):
    class Meta:
        model = Membrepublicateur
        fields = ['nom','prenom','classe','email','numero']




######################################### Formulaire pour ajouter les

class CoursForm(forms.ModelForm):
    class Meta:
        model = Cours
        fields = ['Type_document', 'Titre', 'Matiere_concerné', 'Niveau_concerné', 'Support', 'Description']



class SujetForm(forms.ModelForm):
    class Meta:
        model = Sujet
        fields = ['Type_test', 'Type_sujet', 'Année', 'Niveau', 'Support']



class EvenementForm(forms.ModelForm):
    class Meta:
        model = Evenement
        fields = ['Type_support', 'Titre', 'Description', 'Support']

