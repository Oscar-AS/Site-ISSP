# Generated by Django 4.2.2 on 2023-09-10 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0008_sujet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('sujet', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=1000)),
                ('date_envoi', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]