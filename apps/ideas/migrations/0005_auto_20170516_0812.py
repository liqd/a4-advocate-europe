# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import multiselectfield.db.fields
import django_countries.fields
import autoslug.fields
import adhocracy4.images.fields


class Migration(migrations.Migration):

    dependencies = [
        ('a4modules', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advocate_europe_ideas', '0004_auto_20170512_0845'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('item_ptr', models.OneToOneField(primary_key=True, to='a4modules.Item', serialize=False, auto_created=True, parent_link=True)),
                ('first_name', models.CharField(max_length=250, help_text='Your first name and last name will be published together with the proposal.')),
                ('last_name', models.CharField(max_length=250)),
                ('organisation_status', models.CharField(max_length=255, choices=[('non_profit', 'I am applying on behalf of a registered non-profit organisation, e.g. NGO'), ('non_profit_planned', 'Registration as a non-profit organisation is planned or is already underway'), ('no_non_profit', 'I have a really good idea, but will need help to register a non-profit organisation'), ('other', 'Other')])),
                ('organisation_status_extra', models.TextField(max_length=200, help_text='If you selected other, please clarify your current status. How can we help you? (max. 200 characters)', blank=True)),
                ('organisation_name', models.CharField(max_length=250, help_text='Also if you do not yet have a registered organisation, please write here the name of your initiative or planned organisation.', blank=True)),
                ('organisation_website', models.URLField(max_length=250, blank=True)),
                ('organisation_country', django_countries.fields.CountryField(max_length=2, blank=True)),
                ('organisation_city', models.CharField(max_length=250, blank=True)),
                ('contact_email', models.EmailField(max_length=254, blank=True)),
                ('year_of_registration', models.IntegerField(null=True, blank=True)),
                ('reach_out', models.CharField(max_length=300, help_text='What kind of advice, comments or feedback would you like to receive about your idea from others on the platform? (max. 300 characters)', verbose_name='Reach out – get feedback, ideas and inspiration from the Advocate Europe Community!', blank=True)),
                ('how_did_you_hear', models.CharField(max_length=255, choices=[('personal_contact', 'Personal contact'), ('websites', 'Websites'), ('facebook', 'Facebook'), ('twitter', 'Twitter'), ('newsletter', 'Newsletter'), ('other', 'Other')], verbose_name='How did you hear about Advocate Europe?')),
                ('total_budget', models.IntegerField(help_text='Please indicate your overall budget. The total budget may (but does not have to) include the applicant’s own contribution and/or external sources of funding.', verbose_name='Total Budget')),
                ('budget_requested', models.IntegerField(help_text='Funding requested from Advocate Europe can range from 1 to 50,000 EUR. Depending on your planning, the amount entered here can be the same as the “total budget” figure entered above.', verbose_name='Funding requested from Advocate Europe')),
                ('major_expenses', models.TextField(max_length=500, help_text='Which are the major expenses you foresee for the implementation of your idea? Please share a rough estimate by cost category (e.g. office expenses 1000 EUR, travel and accommodation costs 3000 EUR, public relations 2000 EUR, personnel costs etc.)', verbose_name='Major expenses')),
                ('other_sources', models.BooleanField(help_text='This will not be published and will only be seen by the Advocate Europe team and the jury. Do you anticipate receiving funding for your activity or initiative from other sources (e.g. own contribution, other grants or financial aid)?', verbose_name='Other sources of income')),
                ('other_sources_secured', models.NullBooleanField(help_text='If yes, have these already been secured?', verbose_name='Are these financial sources secured? Yes/no')),
                ('idea_title', models.CharField(max_length=50, help_text='Give your idea a short and meaningful title (max. 50 characters).')),
                ('idea_subtitle', models.CharField(max_length=100, help_text='(max. 100 characters)', blank=True)),
                ('idea_pitch', models.TextField(max_length=500, help_text='Present your idea in 500 characters. Share a concise and attractive text that makes the reader curious. Try to pitch your main challenge, objective, method and target group in 3-5 sentences.')),
                ('idea_image', adhocracy4.images.fields.ConfiguredImageField('idea_image', upload_to='ideas/images', help_text='Upload a photo or illustration that visually supports or explains your idea. Make sure that you have the property rights to share this picture. You can upload a .jpg, .png or .gif of up to 3 MB in size. The image should be in landscape (not portrait) format and have a width of at least 400 pixels.', blank=True)),
                ('idea_topics', multiselectfield.db.fields.MultiSelectField(max_length=255, choices=[('democracy_participation', 'Democracy and participation'), ('arts_cultural_activities', 'Arts and (inter-)cultural activities'), ('environment', 'Environment'), ('social_inclusion', 'Social inclusion'), ('migration', 'Migration'), ('communities', 'Communities'), ('urban_development', 'Urban development'), ('education', 'Education')], help_text='Please select one or two topics for your project.')),
                ('idea_topics_other', models.CharField(max_length=250, blank=True)),
                ('idea_location', multiselectfield.db.fields.MultiSelectField(max_length=250, choices=[('city', 'City, country or region'), ('online', 'Online'), ('ruhr_linkage', 'Linkage to the Ruhr area of Germany')], help_text='Please indicate the location of your project. Choose all options that apply. One to three choices possible.')),
                ('idea_location_specify', models.TextField(max_length=100, help_text='Please specify the city, country and region, e.g. Berlin, Germany', blank=True)),
                ('idea_location_ruhr', models.TextField(max_length=200, help_text='If you selected Ruhr area, please explain. Is your project connected to the Ruhr area of Germany through project partners, audiences, or in some other way? Please provide further details. (max. 200 characters)', blank=True)),
                ('challenge', models.TextField(max_length=300, help_text='Please look here for more information about the annual theme: (link to subpage with more detailed explanation of the annual theme). (max. 300 characters)', verbose_name='What problem or societal need are you working on?')),
                ('outcome', models.TextField(max_length=300, help_text='If your project is selected, what will be different a year from now? What will have changed? Please look here for more information: (link to subpage with explanation on impact). (max. 300 characters)', verbose_name='What would be a successful outcome for your project?')),
                ('plan', models.TextField(max_length=500, help_text='Describe as concretely as possible the approach and / or the method you will use when implementing your idea. What are the steps you plan to take? Please look here for more information: (link to subpage on with explanation on implementation). (max. 500 characters)', verbose_name='How do you plan to get there? Remember to highlight what makes your project design or idea different and innovative.')),
                ('importance', models.TextField(max_length=300, help_text='What motivates you to bring this idea to life? What is your story? What is your personal connection and individual mission behind the idea? (max. 300 characters)', verbose_name='Why is this idea important to you?')),
                ('target_group', models.TextField(max_length=300, help_text='Which target groups, stakeholders, beneficiaries or audiences are at the centre of your project? (max. 300 characters)', verbose_name='Who are you doing it for?')),
                ('members', models.TextField(max_length=500, help_text='Please introduce us to the main members of your project team and briefly summariese their experience and skills. (max. 500 characters)', verbose_name='Who is in your project team?')),
                ('partner_organisation_1_name', models.CharField(max_length=250, verbose_name='name', blank=True)),
                ('partner_organisation_1_website', models.URLField(verbose_name='website', blank=True)),
                ('partner_organisation_1_country', django_countries.fields.CountryField(max_length=2, verbose_name='country', blank=True)),
                ('partner_organisation_2_name', models.CharField(max_length=250, verbose_name='name', blank=True)),
                ('partner_organisation_2_website', models.URLField(verbose_name='website', blank=True)),
                ('partner_organisation_2_country', django_countries.fields.CountryField(max_length=2, verbose_name='country', blank=True)),
                ('partner_organisation_3_name', models.CharField(max_length=250, verbose_name='name', blank=True)),
                ('partner_organisation_3_website', models.URLField(verbose_name='website', blank=True)),
                ('partner_organisation_3_country', django_countries.fields.CountryField(max_length=2, verbose_name='country', blank=True)),
                ('partners_more_info', models.TextField(max_length=200, help_text='Please use this field if you have more than 3 partner organisations or if you want to tell us more about your proposed partnership arrangements (max. 200 characters).', blank=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='idea_title', unique=True)),
                ('duration', models.IntegerField(help_text='How many months will it take to implement your project?', verbose_name='Duration of project (number of months)')),
                ('is_winner', models.BooleanField(default=False)),
                ('jury_statement', models.TextField(verbose_name='Why this idea?', blank=True)),
                ('collaborators', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True)),
                ('idea_sketch', models.OneToOneField(to='advocate_europe_ideas.IdeaSketch')),
            ],
            options={
                'abstract': False,
                'ordering': ['-created'],
            },
            bases=('a4modules.item', models.Model),
        ),
        migrations.RemoveField(
            model_name='ideacomplete',
            name='collaborators',
        ),
        migrations.RemoveField(
            model_name='ideacomplete',
            name='idea_sketch',
        ),
        migrations.RemoveField(
            model_name='ideacomplete',
            name='item_ptr',
        ),
        migrations.DeleteModel(
            name='IdeaComplete',
        ),
    ]
