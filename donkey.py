#import system-relevant packages
import os
import sys

#import django packages
from django.conf import settings

BASE_DIR = os.path.dirname(__file__)

settings.configure(
    DEBUG = True,
    ROOT_URLCONF = 'builder.urls',
    INSTALLED_APPS = (
	'builder',
	'django.contrib.staticfiles',
    ),
    #Put all generated files in GENERATED_SITE_DIR
    GENERATED_SITE_DIR = os.path.join(BASE_DIR, 'generated_site'),
    STATIC_ROOT = os.path.join(BASE_DIR, 'generated_site', 'static'),
)


if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)