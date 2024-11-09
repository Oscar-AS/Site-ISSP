from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['nom', 'prenom', 'email', 'sujet', 'message']

#class Cours_recherche_Form(forms.ModelForm):
 #   indice_T = forms.CharField(label ='Rechercher par ', max_length = 50)
  #  indice_A = forms.CharField(label ='Rechercher par année', max_length=10)
   # fields = ['indice_T']