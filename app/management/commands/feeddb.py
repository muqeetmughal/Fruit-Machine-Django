__author__ = "muqeetmughal786@gmail.com"

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission


User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.init_super_admin()


    def init_super_admin(self):
        self.stdout.write(self.style.WARNING("Initializing Super Admin"))
        username="admin"
        email = "admin@gmail.com"
        password = "admin"
        user = User.objects.filter(email=email).first()
        if not user:
            # for user in settings.ADMINS:

            print("Creating account for (%s)" % email)
            admin = User.objects.create_superuser(username=username,email=email, password=password)
            admin.is_active = True
            admin.save()
        else:
            print("Admin accounts can only be initialized if no Accounts exist")
