# cours/management/commands/check_invalid_foreign_keys.py

from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Check for invalid foreign keys in cours_evenement'

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT * FROM cours_evenement WHERE Auteur_id NOT IN (SELECT id FROM auth_user)
            """)
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    self.stdout.write(self.style.ERROR(f'Invalid row: {row}'))
            else:
                self.stdout.write(self.style.SUCCESS('No invalid foreign keys found.'))
