# Generated by Django 4.2.2 on 2024-01-04 14:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0025_demandepublicateur_delete_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='sujet',
            name='Niveau',
            field=models.CharField(choices=[('option1', 'Bac'), ('option2', 'Licence')], default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
