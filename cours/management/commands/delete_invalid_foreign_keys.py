# cours/management/commands/delete_invalid_foreign_keys.py

from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Delete invalid foreign keys in cours_evenement'

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute("""
                DELETE FROM cours_evenement WHERE Auteur_id NOT IN (SELECT id FROM auth_user)
            """)
            self.stdout.write(self.style.SUCCESS('Deleted invalid foreign keys.'))
