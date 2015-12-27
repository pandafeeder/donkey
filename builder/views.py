#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from django.http import Http404
from django.shortcuts import render_to_response
from django.conf import settings
from django.template import Template, Context


def get_page_or_404(pagename):
    """get the content page then Template it"""
    pagedir = settings.SITE_PAGE_DIRECTORY
    pagefile_path = os.path.join(pagedir, pagename)
    if not os.path.exists(pagefile_path):
	raise Http404("Page does not exist")
    with open(pagefile_path, 'r') as f:
	page = Template(f.read())
    return page


def page(request, slug='index'):
    """render each page"""
    #pagename = '{}.html'.format(slug)
    pagename = slug+'.html'
    page = get_page_or_404(pagename)
    context = {
	'page': page,
	'slug': slug,
    }
    return render_to_response('page.html', context)
