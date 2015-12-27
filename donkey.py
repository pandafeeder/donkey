#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import system-relevant packages
import os
import sys

#import django packages
from django.conf import settings

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

settings.configure(
    DEBUG = True,
    ROOT_URLCONF = 'builder.urls',
    INSTALLED_APPS = (
	'django.contrib.staticfiles',
	'builder',
    ),
    STATIC_URL = '/static/',
    SITE_PAGE_DIRECTORY = os.path.join(BASE_DIR, 'pages'),
    #Put all generated files in GENERATED_SITE_DIR
    GENERATED_SITE_DIR = os.path.join(BASE_DIR, 'generated_site'),
    #set SATIC_ROOT to enalbe django command collectstatc for finally puts all static file in this dir
    STATIC_ROOT = os.path.join(BASE_DIR, 'generated_site', 'static'),
    TEMPLATES = [
	{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
		],
	    },
	},
    ],
)


if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
