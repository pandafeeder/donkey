# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help ="""Crawler to craw web blog"""

    def add_arguments(self, parser):
	parser.add_argument('web_site')

    def handle(self, **options):
	url = options['web_site']
	if not 'http' in url:
	    url = 'http://'+url
	try:
	    response = requests.get(url)
	except:
	    print "Failed to request "+url
	html_doc = response.text
	soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')
	links = soup.find_all('a', href=re.compile(r'posts'))

	inner_urls = set()
	for link in links:
	    inner_urls.add(url+link['href'])

	for inner_url in sorted(inner_urls):
	    html_doc = requests.get(inner_url).text
	    soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')
	    html_file_name = soup.h3.get_text().replace(' ', '_').replace('.', '_')
	    with open(settings.SITE_PAGE_DIRECTORY+'/'+html_file_name+'.html', 'w') as f:
		f.write(str(soup.find(id='content')))
