# Generated by Django 4.2.2 on 2024-01-17 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0031_commentaire_remove_userprofile_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mots',
            name='Mot',
            field=models.CharField(max_length=3000),
        ),
        migrations.DeleteModel(
            name='Commentaire',
        ),
    ]
