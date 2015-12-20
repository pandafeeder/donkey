import os
import shutil

from django.conf import settings
from django.core.management import call_command
from django.core.managemant.base import BaseCommand, CommandError
from django.core.urlresolvers import reverse
from django.test.client import Client
