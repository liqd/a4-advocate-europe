import csv
import re

from allauth.account.models import EmailAddress
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand

User = get_user_model()


def fixup_username(username):
    return re.sub(r'[^ \w.+\-@]', '_', username).lstrip('+-.@ _')


class Command(BaseCommand):
    help = 'Import users from csv file exported with A3'

    def add_arguments(self, parser):
        parser.add_argument('inputfile', type=str)

    def handle(self, inputfile, *args, **options):
        with open(inputfile) as f:
            reader = csv.DictReader(f, delimiter=';')

            for user in reader:
                self._add_user(user)

    def _add_user(self, userdata):
        email = userdata['Email']
        original_username = userdata['Username']
        username = fixup_username(original_username)

        user_exists = User.objects.filter(
            email=email, username=username
        ).exists()

        user = User(
            username=username,
            email=email,
            date_joined=userdata['Creation date'],
            password="bcrypt$" + userdata['Password hash'],
        )

        if user_exists:
            print(
                'Skipping user {} <{}> because already exists'.format(
                    user.username, user.email
                )
            )
            return

        try:
            user.full_clean()
        except ValidationError as e:
            if 'email' in e.error_dict:
                print(
                    'Skipping user {} <{}> due to invalid email'.format(
                        user.username, user.email
                    )
                )
                return
            else:
                import sys
                print(
                    'Aborting due to user {} <{}> with {}'.format(
                        user.username, user.email, e
                    )
                )
                sys.exit('Invalid user')

        user.save()
        email = EmailAddress(
            user=user,
            email=userdata['Email'],
            verified=True,
            primary=True,
        )
        email.save()
