# Generated by Django 4.2.2 on 2024-07-24 00:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cours', '0039_remove_cours_consultation_delete_adminrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cours',
            name='Date_actualisation',
        ),
        migrations.RemoveField(
            model_name='evenement',
            name='Classe_auteur',
        ),
        migrations.RemoveField(
            model_name='evenement',
            name='Consultation',
        ),
        migrations.RemoveField(
            model_name='evenement',
            name='Date_actualisation',
        ),
        migrations.RemoveField(
            model_name='sujet',
            name='Consultation',
        ),
        migrations.RemoveField(
            model_name='sujet',
            name='Date_actualisation',
        ),
        migrations.AlterField(
            model_name='evenement',
            name='Auteur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sujet',
            name='Auteur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]