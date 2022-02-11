from django.core.management.base import BaseCommand
from django.core import management


class Command(BaseCommand):
    help = 'Fast migrate and run server over http'

    def handle(self, *args, **options):
        management.call_command('makemigrations')
        management.call_command('migrate')
        management.call_command('runserver')