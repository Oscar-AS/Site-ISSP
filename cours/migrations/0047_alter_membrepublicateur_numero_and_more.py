# Generated by Django 4.2.2 on 2024-07-24 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0046_alter_membrepublicateur_numero_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membrepublicateur',
            name='numero',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='membrepublicateur',
            name='status',
            field=models.CharField(choices=[('En attente', 'En attente'), ('Accepter', 'Accepter'), ('Rejetter', 'Rejetter')], default='En attente', max_length=15),
        ),
    ]
