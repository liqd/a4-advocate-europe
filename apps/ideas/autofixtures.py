from autofixture import AutoFixture, generators, register
from faker import Factory

from .models import IdeaComplete, IdeaSketch

fake = Factory.create()


class IdeaSketchAutoFixture(AutoFixture):

    IMAGESIZES = ((800, 600),)

    field_values = {
        'first_name': generators.CallableGenerator(fake.first_name),
        'last_name': generators.CallableGenerator(fake.last_name),
        'organisation_name': generators.CallableGenerator(fake.company),
        'organisation_city': generators.CallableGenerator(fake.city),
        'contact_email': generators.CallableGenerator(fake.email),
        'year_of_registration': generators.CallableGenerator(fake.year),

        'idea_pitch': generators.CallableGenerator(fake.text),
        'idea_image': generators.ImageGenerator(sizes=IMAGESIZES),
        'idea_location_specify': generators.CallableGenerator(fake.city),

        'partner_organisation_1_name':
            generators.CallableGenerator(fake.company),
        'partner_organisation_2_name':
            generators.CallableGenerator(fake.company),
        'partner_organisation_3_name':
            generators.CallableGenerator(fake.company),
    }

    follow_pk = True
    follow_fk = True

register(IdeaSketch, IdeaSketchAutoFixture)


class IdeaCompleteAutoFixture(AutoFixture):

    IMAGESIZES = ((800, 600),)

    field_values = {
        'first_name': generators.CallableGenerator(fake.first_name),
        'last_name': generators.CallableGenerator(fake.last_name),
        'organisation_name': generators.CallableGenerator(fake.company),
        'organisation_city': generators.CallableGenerator(fake.city),
        'contact_email': generators.CallableGenerator(fake.email),
        'year_of_registration': generators.CallableGenerator(fake.year),

        'idea_pitch': generators.CallableGenerator(fake.text),
        'idea_image': generators.ImageGenerator(sizes=IMAGESIZES),
        'idea_location_specify': generators.CallableGenerator(fake.city),

        'partner_organisation_1_name':
            generators.CallableGenerator(fake.company),
        'partner_organisation_2_name':
            generators.CallableGenerator(fake.company),
        'partner_organisation_3_name':
            generators.CallableGenerator(fake.company),
    }

    follow_pk = True
    follow_fk = True


register(IdeaComplete, IdeaCompleteAutoFixture)
