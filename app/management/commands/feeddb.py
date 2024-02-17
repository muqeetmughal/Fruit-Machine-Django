__author__ = "muqeetmughal786@gmail.com"

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from tenants.models import Client

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.init_super_admin()
        self.assign_permissions_to_group()
        self.create_public_tenant()
        self.create_default_tenants()
        call_command("scrape_countries")

    def create_public_tenant(self):
        self.stdout.write(self.style.WARNING("Creating Public Tenant..."))
        call_command("createpublictenant")

    def create_default_tenants(self):
        self.stdout.write(self.style.WARNING("Initializing Default Tenants..."))
        try:
            Client.objects.get_or_create(
                schema_name="muqeet",
                phone_number="3096699016",
                email="muqeetmughal786@gmail.com",
                is_phone_verified=True,
                is_email_verified=True,
                on_trial=True,
                is_active=True,
            )
        except Exception as e:
            self.stdout.write(self.style.ERROR(str(e)))

    def assign_permissions_to_group(self):
        self.stdout.write(self.style.WARNING("Initializing Group Permissions"))
        group, created = Group.objects.get_or_create(name="Client")
        client_app_permissions = Permission.objects.filter(
            content_type__app_label="client"
        )
        group.permissions.add(*client_app_permissions)

    def init_super_admin(self):
        self.stdout.write(self.style.WARNING("Initializing Super Admin"))

        email = "admin@gmail.com"
        password = "admin"
        user = User.objects.filter(email=email).first()
        if not user:
            # for user in settings.ADMINS:

            print("Creating account for (%s)" % email)
            admin = User.objects.create_superuser(email=email, password=password)
            admin.is_active = True
            admin.save()
        else:
            print("Admin accounts can only be initialized if no Accounts exist")

    # def create_units(self):
    #     print("Initializing Units")
    #     client_models.Unit.objects.get_or_create(name="Kilogram", code="kg")
    #     client_models.Unit.objects.get_or_create(name="Unit", code="unit")
    #     client_models.Unit.objects.get_or_create(name=" ", code="pcs")
