# Generated by Django 4.2.2 on 2024-02-26 01:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cours', '0032_alter_mots_mot_delete_commentaire'),
    ]

    operations = [
        migrations.CreateModel(
            name='MembershipRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('En attente', 'En attente'), ('Accepter', 'Accepter'), ('Rejetter', 'Rejetter')], default='En attente', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]