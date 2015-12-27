# -*- coding: utf-8 -*-

import os
import shutil

import requests

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.core.urlresolvers import reverse
from django.test.client import Client


def get_pages():
    """get every single page in pages dir"""
    if not os.path.exists(settings.SITE_PAGE_DIRECTORY):
	raise Exception(settings.SITE_PAGE_DIRECTORY+" does not exist")

    pages = os.listdir(settings.SITE_PAGE_DIRECTORY)

    if not pages:
	raise Exception("No file in "+settings.SITE_PAGE_DIRECTORY)
    for page in pages:
	if page.endswith('.html'):
	    #print page
	    yield page[:-5]


class Command(BaseCommand):
    help = """Request pages and build output"""

    def add_arguments(self, parser):
	parser.add_argument('args', nargs='*')

    def handle(self, **options):
	#options['page']
	pages = get_pages()
	if not os.path.exists(settings.GENERATED_SITE_DIR):
	    os.mkdir(settings.GENERATED_SITE_DIR)
	if not os.path.exists(settings.STATIC_ROOT):
	    os.mkdir(settings.STATIC_ROOT)
	client = Client()
	for page in pages:
	    url = reverse('page', kwargs = {'slug': page})
	    response = client.get(url)
	    output_dir = os.path.join(settings.GENERATED_SITE_DIR, page)
	    if not os.path.exists(output_dir):
		os.mkdir(output_dir)
	    with open(os.path.join(output_dir, 'index.html'), 'wb') as f:
		f.write(response.content)
