import os
import shutil

import requests

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.core.urlresolvers import reverse


class Command(BaseCommand):
    help = """Request pages and build output"""

    def add_arguments(self, parser):
	parser.add_argument('page')

    def handle(self, **options):
	options['page']
