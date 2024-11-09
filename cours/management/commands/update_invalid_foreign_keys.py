# cours/management/commands/update_invalid_foreign_keys.py

from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Update invalid foreign keys in cours_evenement'

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE cours_evenement SET Auteur_id = (SELECT id FROM auth_user LIMIT 1) WHERE Auteur_id NOT IN (SELECT id FROM auth_user)
            """)  # Remplace `(SELECT id FROM auth_user LIMIT 1)` par un id valide de la table `auth_user` si nécessaire
            self.stdout.write(self.style.SUCCESS('Updated invalid foreign keys.'))
