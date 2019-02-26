# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields
import django_countries.fields
import adhocracy4.images.fields
import django.utils.timezone
from django.conf import settings
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('a4modules', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, primary_key=True, parent_link=True, serialize=False, to='a4modules.Item', on_delete=models.CASCADE)),
                ('first_name', models.CharField(help_text='Your first name and last name will be published together with the proposal.', max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('organisation_status', models.CharField(choices=[('non_profit', 'I am applying on behalf of a registered non-profit organisation, e.g. NGO'), ('non_profit_planned', 'Registration as a non-profit organisation is planned or is already underway'), ('no_non_profit', 'I have a really good idea, but will need help to register a non-profit organisation'), ('other', 'Other')], max_length=255)),
                ('organisation_status_extra', models.TextField(blank=True, max_length=200, help_text='If you selected other, please clarify your current status. How can we help you? (max. 200 characters)')),
                ('organisation_name', models.CharField(blank=True, max_length=250, help_text='Also if you do not yet have a registered organisation, please write here the name of your initiative or planned organisation.')),
                ('organisation_website', models.URLField(blank=True, max_length=250)),
                ('organisation_country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('organisation_city', models.CharField(blank=True, max_length=250)),
                ('contact_email', models.EmailField(blank=True, max_length=254)),
                ('year_of_registration', models.IntegerField(blank=True, null=True)),
                ('reach_out', models.TextField(blank=True, verbose_name='Reach out – get feedback, ideas and inspiration from the Advocate Europe Community!', max_length=300, help_text='What kind of advice, comments or feedback would you like to receive about your idea from others on the platform? (max. 300 characters)')),
                ('how_did_you_hear', models.CharField(choices=[('personal_contact', 'Personal contact'), ('websites', 'Websites'), ('facebook', 'Facebook'), ('twitter', 'Twitter'), ('newsletter', 'Newsletter'), ('other', 'Other')], verbose_name='How did you hear about Advocate Europe?', max_length=255)),
                ('idea_title', models.CharField(help_text='Give your idea a short and meaningful title (max. 50 characters).', max_length=50)),
                ('idea_subtitle', models.CharField(blank=True, max_length=100, help_text='(max. 100 characters)')),
                ('idea_pitch', models.TextField(help_text='Present your idea in 500 characters. Share a concise and attractive text that makes the reader curious. Try to pitch your main challenge, objective, method and target group in 3-5 sentences.', max_length=500)),
                ('idea_image', adhocracy4.images.fields.ConfiguredImageField('idea_image', upload_to='ideas/images', blank=True, help_text='Upload a photo or illustration that visually supports or explains your idea. Make sure that you have the property rights to share this picture. You can upload a .jpg, .png or .gif of up to 3 MB in size. The image should be in landscape (not portrait) format and have a width of at least 400 pixels.')),
                ('idea_topics', multiselectfield.db.fields.MultiSelectField(help_text='Please select one or two topics for your project.', choices=[('democracy_participation', 'Democracy and participation'), ('arts_cultural_activities', 'Arts and (inter-)cultural activities'), ('environment', 'Environment'), ('social_inclusion', 'Social inclusion'), ('migration', 'Migration'), ('communities', 'Communities'), ('urban_development', 'Urban development'), ('education', 'Education')], max_length=255)),
                ('idea_topics_other', models.CharField(blank=True, max_length=250)),
                ('idea_location', multiselectfield.db.fields.MultiSelectField(help_text='Please indicate the location of your project. Choose all options that apply. One to three choices possible.', choices=[('city', 'City, country or region'), ('online', 'Online'), ('ruhr_linkage', 'Linkage to the Ruhr area of Germany')], max_length=250)),
                ('idea_location_specify', models.TextField(blank=True, max_length=100, help_text='Please specify the city, country and region, e.g. Berlin, Germany')),
                ('idea_location_ruhr', models.TextField(blank=True, max_length=200, help_text='If you selected Ruhr area, please explain. Is your project connected to the Ruhr area of Germany through project partners, audiences, or in some other way? Please provide further details. (max. 200 characters)')),
                ('challenge', models.TextField(help_text='Please look here for more information about the annual theme: (link to subpage with more detailed explanation of the annual theme). (max. 300 characters)', verbose_name='What problem or societal need are you working on?', max_length=300)),
                ('outcome', models.TextField(help_text='If your project is selected, what will be different a year from now? What will have changed? Please look here for more information: (link to subpage with explanation on impact). (max. 300 characters)', verbose_name='What would be a successful outcome for your project?', max_length=300)),
                ('plan', models.TextField(help_text='Describe as concretely as possible the approach and / or the method you will use when implementing your idea. What are the steps you plan to take? Please look here for more information: (link to subpage on with explanation on implementation). (max. 500 characters)', verbose_name='How do you plan to get there? Remember to highlight what makes your project design or idea different and innovative.', max_length=500)),
                ('importance', models.TextField(help_text='What motivates you to bring this idea to life? What is your story? What is your personal connection and individual mission behind the idea? (max. 300 characters)', verbose_name='Why is this idea important to you?', max_length=300)),
                ('target_group', models.TextField(help_text='Which target groups, stakeholders, beneficiaries or audiences are at the centre of your project? (max. 300 characters)', verbose_name='Who are you doing it for?', max_length=300)),
                ('members', models.TextField(help_text='Please introduce us to the main members of your project team and briefly summariese their experience and skills. (max. 500 characters)', verbose_name='Who is in your project team?', max_length=500)),
                ('partner_organisation_1_name', models.CharField(blank=True, verbose_name='name', max_length=250)),
                ('partner_organisation_1_website', models.URLField(blank=True, verbose_name='website')),
                ('partner_organisation_1_country', django_countries.fields.CountryField(blank=True, verbose_name='country', max_length=2)),
                ('partner_organisation_2_name', models.CharField(blank=True, verbose_name='name', max_length=250)),
                ('partner_organisation_2_website', models.URLField(blank=True, verbose_name='website')),
                ('partner_organisation_2_country', django_countries.fields.CountryField(blank=True, verbose_name='country', max_length=2)),
                ('partner_organisation_3_name', models.CharField(blank=True, verbose_name='name', max_length=250)),
                ('partner_organisation_3_website', models.URLField(blank=True, verbose_name='website')),
                ('partner_organisation_3_country', django_countries.fields.CountryField(blank=True, verbose_name='country', max_length=2)),
                ('partners_more_info', models.TextField(blank=True, max_length=200, help_text='Please use this field if you have more than 3 partner organisations or if you want to tell us more about your proposed partnership arrangements (max. 200 characters).')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='idea_title', unique=True)),
                ('visit_camp', models.BooleanField(default=False)),
                ('is_winner', models.BooleanField(default=False)),
                ('community_award_winner', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
                'ordering': ['-created'],
            },
            bases=('a4modules.item', models.Model),
        ),
        migrations.CreateModel(
            name='IdeaSketchArchived',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(editable=False, default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(editable=False, blank=True, null=True)),
                ('first_name', models.CharField(help_text='Your first name and last name will be published together with the proposal.', max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('organisation_status', models.CharField(choices=[('non_profit', 'I am applying on behalf of a registered non-profit organisation, e.g. NGO'), ('non_profit_planned', 'Registration as a non-profit organisation is planned or is already underway'), ('no_non_profit', 'I have a really good idea, but will need help to register a non-profit organisation'), ('other', 'Other')], max_length=255)),
                ('organisation_status_extra', models.TextField(blank=True, max_length=200, help_text='If you selected other, please clarify your current status. How can we help you? (max. 200 characters)')),
                ('organisation_name', models.CharField(blank=True, max_length=250, help_text='Also if you do not yet have a registered organisation, please write here the name of your initiative or planned organisation.')),
                ('organisation_website', models.URLField(blank=True, max_length=250)),
                ('organisation_country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('organisation_city', models.CharField(blank=True, max_length=250)),
                ('contact_email', models.EmailField(blank=True, max_length=254)),
                ('year_of_registration', models.IntegerField(blank=True, null=True)),
                ('collaboration_camp_option', models.CharField(help_text='Choose one of the following options. More information about the two tracks is available here: (Link).', choices=[('single_track', 'Single track'), ('partner_track', 'Partner track'), ('not_sure', "I'm not sure yet")], max_length=255)),
                ('collaboration_camp_represent', models.TextField(help_text='(Specify one person only. (max 150 characters))', verbose_name='Who will represent your idea at the Collaboration Camp and why?', max_length=150)),
                ('collaboration_camp_email', models.EmailField(verbose_name='Email address for contacting your representative on the collaboration camp.', max_length=254)),
                ('collaboration_camp_benefit', models.TextField(help_text="Tell us about your expectations. Think about your skills, resources, networks and partners when describing what you could offer and what you'd like to take away. (max. 300 characters)", verbose_name='How could you contribute to and benefit from participating in the Collaboration Camp?', max_length=300)),
                ('reach_out', models.TextField(blank=True, verbose_name='Reach out – get feedback, ideas and inspiration from the Advocate Europe Community!', max_length=300, help_text='What kind of advice, comments or feedback would you like to receive about your idea from others on the platform? (max. 300 characters)')),
                ('how_did_you_hear', models.CharField(choices=[('personal_contact', 'Personal contact'), ('websites', 'Websites'), ('facebook', 'Facebook'), ('twitter', 'Twitter'), ('newsletter', 'Newsletter'), ('other', 'Other')], verbose_name='How did you hear about Advocate Europe?', max_length=255)),
                ('idea_title', models.CharField(help_text='Give your idea a short and meaningful title (max. 50 characters).', max_length=50)),
                ('idea_subtitle', models.CharField(blank=True, max_length=100, help_text='(max. 100 characters)')),
                ('idea_pitch', models.TextField(help_text='Present your idea in 500 characters. Share a concise and attractive text that makes the reader curious. Try to pitch your main challenge, objective, method and target group in 3-5 sentences.', max_length=500)),
                ('idea_image', adhocracy4.images.fields.ConfiguredImageField('idea_image', upload_to='ideas/images', blank=True, help_text='Upload a photo or illustration that visually supports or explains your idea. Make sure that you have the property rights to share this picture. You can upload a .jpg, .png or .gif of up to 3 MB in size. The image should be in landscape (not portrait) format and have a width of at least 400 pixels.')),
                ('idea_topics', multiselectfield.db.fields.MultiSelectField(help_text='Please select one or two topics for your project.', choices=[('democracy_participation', 'Democracy and participation'), ('arts_cultural_activities', 'Arts and (inter-)cultural activities'), ('environment', 'Environment'), ('social_inclusion', 'Social inclusion'), ('migration', 'Migration'), ('communities', 'Communities'), ('urban_development', 'Urban development'), ('education', 'Education')], max_length=255)),
                ('idea_topics_other', models.CharField(blank=True, max_length=250)),
                ('idea_location', multiselectfield.db.fields.MultiSelectField(help_text='Please indicate the location of your project. Choose all options that apply. One to three choices possible.', choices=[('city', 'City, country or region'), ('online', 'Online'), ('ruhr_linkage', 'Linkage to the Ruhr area of Germany')], max_length=250)),
                ('idea_location_specify', models.TextField(blank=True, max_length=100, help_text='Please specify the city, country and region, e.g. Berlin, Germany')),
                ('idea_location_ruhr', models.TextField(blank=True, max_length=200, help_text='If you selected Ruhr area, please explain. Is your project connected to the Ruhr area of Germany through project partners, audiences, or in some other way? Please provide further details. (max. 200 characters)')),
                ('challenge', models.TextField(help_text='Please look here for more information about the annual theme: (link to subpage with more detailed explanation of the annual theme). (max. 300 characters)', verbose_name='What problem or societal need are you working on?', max_length=300)),
                ('outcome', models.TextField(help_text='If your project is selected, what will be different a year from now? What will have changed? Please look here for more information: (link to subpage with explanation on impact). (max. 300 characters)', verbose_name='What would be a successful outcome for your project?', max_length=300)),
                ('plan', models.TextField(help_text='Describe as concretely as possible the approach and / or the method you will use when implementing your idea. What are the steps you plan to take? Please look here for more information: (link to subpage on with explanation on implementation). (max. 500 characters)', verbose_name='How do you plan to get there? Remember to highlight what makes your project design or idea different and innovative.', max_length=500)),
                ('importance', models.TextField(help_text='What motivates you to bring this idea to life? What is your story? What is your personal connection and individual mission behind the idea? (max. 300 characters)', verbose_name='Why is this idea important to you?', max_length=300)),
                ('target_group', models.TextField(help_text='Which target groups, stakeholders, beneficiaries or audiences are at the centre of your project? (max. 300 characters)', verbose_name='Who are you doing it for?', max_length=300)),
                ('members', models.TextField(help_text='Please introduce us to the main members of your project team and briefly summariese their experience and skills. (max. 500 characters)', verbose_name='Who is in your project team?', max_length=500)),
                ('partner_organisation_1_name', models.CharField(blank=True, verbose_name='name', max_length=250)),
                ('partner_organisation_1_website', models.URLField(blank=True, verbose_name='website')),
                ('partner_organisation_1_country', django_countries.fields.CountryField(blank=True, verbose_name='country', max_length=2)),
                ('partner_organisation_2_name', models.CharField(blank=True, verbose_name='name', max_length=250)),
                ('partner_organisation_2_website', models.URLField(blank=True, verbose_name='website')),
                ('partner_organisation_2_country', django_countries.fields.CountryField(blank=True, verbose_name='country', max_length=2)),
                ('partner_organisation_3_name', models.CharField(blank=True, verbose_name='name', max_length=250)),
                ('partner_organisation_3_website', models.URLField(blank=True, verbose_name='website')),
                ('partner_organisation_3_country', django_countries.fields.CountryField(blank=True, verbose_name='country', max_length=2)),
                ('partners_more_info', models.TextField(blank=True, max_length=200, help_text='Please use this field if you have more than 3 partner organisations or if you want to tell us more about your proposed partnership arrangements (max. 200 characters).')),
                ('collaborators', models.ManyToManyField(blank=True, related_name='ideasketcharchived_collaborators', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IdeaSketch',
            fields=[
                ('idea_ptr', models.OneToOneField(auto_created=True, primary_key=True, parent_link=True, serialize=False, to='advocate_europe_ideas.Idea', on_delete=models.CASCADE)),
                ('collaboration_camp_option', models.CharField(help_text='Choose one of the following options. More information about the two tracks is available here: (Link).', choices=[('single_track', 'Single track'), ('partner_track', 'Partner track'), ('not_sure', "I'm not sure yet")], max_length=255)),
                ('collaboration_camp_represent', models.TextField(help_text='(Specify one person only. (max 150 characters))', verbose_name='Who will represent your idea at the Collaboration Camp and why?', max_length=150)),
                ('collaboration_camp_email', models.EmailField(verbose_name='Email address for contacting your representative on the collaboration camp.', max_length=254)),
                ('collaboration_camp_benefit', models.TextField(help_text="Tell us about your expectations. Think about your skills, resources, networks and partners when describing what you could offer and what you'd like to take away. (max. 300 characters)", verbose_name='How could you contribute to and benefit from participating in the Collaboration Camp?', max_length=300)),
            ],
            options={
                'abstract': False,
                'ordering': ['-created'],
            },
            bases=('advocate_europe_ideas.idea', models.Model),
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('idea_ptr', models.OneToOneField(auto_created=True, primary_key=True, parent_link=True, serialize=False, to='advocate_europe_ideas.Idea', on_delete=models.CASCADE)),
                ('total_budget', models.IntegerField(help_text='Please indicate your overall budget. The total budget may (but does not have to) include the applicant’s own contribution and/or external sources of funding.', verbose_name='Total Budget')),
                ('budget_requested', models.IntegerField(help_text='Funding requested from Advocate Europe can range from 1 to 50,000 EUR. Depending on your planning, the amount entered here can be the same as the “total budget” figure entered above.', verbose_name='Funding requested from Advocate Europe')),
                ('major_expenses', models.TextField(help_text='Which are the major expenses you foresee for the implementation of your idea? Please share a rough estimate by cost category (e.g. office expenses 1000 EUR, travel and accommodation costs 3000 EUR, public relations 2000 EUR, personnel costs etc.)', verbose_name='Major expenses', max_length=500)),
                ('other_sources', models.BooleanField(verbose_name='Other sources of income', help_text='This will not be published and will only be seen by the Advocate Europe team and the jury. Do you anticipate receiving funding for your activity or initiative from other sources (e.g. own contribution, other grants or financial aid)?')),
                ('other_sources_secured', models.NullBooleanField(verbose_name='Are these financial sources secured? Yes/no', help_text='If yes, have these already been secured?')),
                ('duration', models.IntegerField(help_text='How many months will it take to implement your project?', verbose_name='Duration of project (number of months)')),
                ('selection_cohesion', models.TextField(verbose_name='How will your idea strengthen connection and cohesion in Europe?', max_length=500)),
                ('selection_apart', models.TextField(help_text='What is surprising or unconventional about your idea? What is special about your idea?', verbose_name='What makes your idea stand apart?', max_length=500)),
                ('selection_relevance', models.TextField(help_text='How will your project connect to, or influence, people’s daily lives?', verbose_name='What is the practical relevance of your idea to people’s everyday lives?', max_length=500)),
                ('jury_statement', models.TextField(blank=True, verbose_name='Why this idea?')),
            ],
            options={
                'abstract': False,
                'ordering': ['-created'],
            },
            bases=('advocate_europe_ideas.idea', models.Model),
        ),
        migrations.AddField(
            model_name='ideasketcharchived',
            name='idea',
            field=models.OneToOneField(to='advocate_europe_ideas.Idea', on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='idea',
            name='collaborators',
            field=models.ManyToManyField(blank=True, related_name='idea_collaborators', to=settings.AUTH_USER_MODEL),
        ),
    ]
