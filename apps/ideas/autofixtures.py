from autofixture import AutoFixture, generators, register
from faker import Factory

from .models import IdeaComplete, IdeaSketch

fake = Factory.create()


class IdeaSketchAutoFixture(AutoFixture):

    IMAGESIZES = ((400, 200), (600, 400), (600, 300), )

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
        'idea_topics_other': generators.ChoicesGenerator(
            values=['', 'Cats', 'Traffic', 'Poverty']
        ),

        'partner_organisation_1_name':
            generators.CallableGenerator(fake.company),
        'partner_organisation_2_name':
            generators.CallableGenerator(fake.company),
        'partner_organisation_3_name':
            generators.CallableGenerator(fake.company),
    }

    follow_pk = True
    generate_fk = True

register(IdeaSketch, IdeaSketchAutoFixture)


class IdeaCompleteAutoFixture(AutoFixture):

    IMAGESIZES = ((400, 200), (600, 400), (600, 300), )

    field_values = IdeaSketchAutoFixture.field_values

    follow_pk = True
    generate_fk = True


register(IdeaComplete, IdeaCompleteAutoFixture)
