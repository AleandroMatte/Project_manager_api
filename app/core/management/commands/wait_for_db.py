'''
Django command to wait for database
'''
import time
from typing import Any
from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError


class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any):
        '''Entry point for comand'''
        self.stdout.write('Waiting for Database...')
        db_up = False
        while not (db_up):
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
