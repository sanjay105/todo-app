from django.core.management.base import BaseCommand, CommandError
import click
class Command(BaseCommand):
    help='Hello sanjay'
    def handle(self, *args, **options):
        
        click.echo(click.style('hello',fg='green'))