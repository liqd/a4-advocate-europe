# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-23 16:18
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_europe_ideas', '0019_change_helptextes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposal',
            name='other_sources',
        ),
        migrations.RemoveField(
            model_name='proposal',
            name='other_sources_secured',
        ),
        migrations.AddField(
            model_name='proposal',
            name='network',
            field=models.TextField(default='-', help_text='The Advocate Europe network includes all previous winning projects, jury members, the online community, the partner organisations Stiftung Mercator, MitOst e.V. and Liquid Democracy e.V. and the Advocate Europe team. Winning projects meet at least one time per year in network meetings. Tell us about your expectations. Think about your skills, resources, networks and partners when describing what you could offer and ‚what you would like to take away. (max. 800 characters)', max_length=800, verbose_name='How will you contribute to and benefit from the Advocate Europe network?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proposal',
            name='selection_advocating',
            field=models.TextField(default='-', help_text='Through what actions, measures or channels will you be reaching out to your key target groups and others to whom your idea is relevant? (max. 800 characters)', max_length=800, verbose_name='How will you be reaching out to others and advocating your idea?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proposal',
            name='selection_key_indicators',
            field=models.TextField(default='-', help_text='What are the key indicators of success of your endeavour in the first year? What are key indicators for failure in the first year? If successful, how will you amplify your successes? If you should fail, how will you recover? (max. 800 characters)', max_length=800, verbose_name='Key Indicators'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='idea',
            name='challenge',
            field=models.TextField(help_text='How does your idea address the challenges of democracy in Europe today? How does it suit our 2017-2018 call for ideas for democracy in Europe? (max. 800 characters)', max_length=800, verbose_name='How will your idea strengthen democracy in Europe?'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='idea_location_ruhr',
            field=models.TextField(blank=True, help_text='Is your project connected to the Ruhr area of Germany through project partners or audiences? Please provide further details. (max. 500 characters)', max_length=500, verbose_name='Links to the Ruhr area'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='idea_topics',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('democracy_participation', 'Democracy and participation'), ('arts_cultural_activities', 'Arts and cultural activities'), ('environment', 'Environment'), ('social_inclusion', 'Social inclusion'), ('migration', 'Migration'), ('communities', 'Communities'), ('urban_development', 'Urban development'), ('education', 'Education')], help_text='Choose 1-2 topics that describe your idea. Your answer to this question does not influence the selection process. It helps us to get a better overview of the proposals we receive.', max_length=255, verbose_name='Topic'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='importance',
            field=models.TextField(help_text='What motivates you to bring this idea to life? What is your story? What is your connection and mission behind the idea? (max. 800 characters)', max_length=800, verbose_name='Why is this idea important to you?'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='members',
            field=models.TextField(help_text='Please introduce us to the main members of your project team and briefly summarise their experience and skills. (max. 800 characters)', max_length=800, verbose_name='Who is in your project team?'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='outcome',
            field=models.TextField(help_text='If your idea is selected, what will be different a year from now? What will have changed? (max. 800 characters)', max_length=800, verbose_name='What would be a successful outcome for your idea?'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='plan',
            field=models.TextField(help_text='Describe as concretely as possible the approach and/or the method you will use when implementing your idea. What are the steps you plan to take? (max. 800 characters)', max_length=800, verbose_name='How do you plan to get there?'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='reach_out',
            field=models.TextField(blank=True, help_text='What kind of advice, comments or feedback would you like to receive about your idea from others on the platform? (max. 300 characters)', max_length=300, verbose_name='Reach out – get feedback, ideas and inspiration from the Advocate Europe online Community!'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='target_group',
            field=models.TextField(help_text='Which target groups, stakeholders, beneficiaries or audiences are at the centre of your idea? (max. 800 characters)', max_length=800, verbose_name='Who are you doing it for and/or with?'),
        ),
        migrations.AlterField(
            model_name='ideasketcharchived',
            name='challenge',
            field=models.TextField(help_text='How does your idea address the challenges of democracy in Europe today? How does it suit our 2017-2018 call for ideas for democracy in Europe? (max. 800 characters)', max_length=800, verbose_name='How will your idea strengthen democracy in Europe?'),
        ),
        migrations.AlterField(
            model_name='ideasketcharchived',
            name='idea_location_ruhr',
            field=models.TextField(blank=True, help_text='Is your project connected to the Ruhr area of Germany through project partners or audiences? Please provide further details. (max. 500 characters)', max_length=500, verbose_name='Links to the Ruhr area'),
        ),
        migrations.AlterField(
            model_name='ideasketcharchived',
            name='idea_topics',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('democracy_participation', 'Democracy and participation'), ('arts_cultural_activities', 'Arts and cultural activities'), ('environment', 'Environment'), ('social_inclusion', 'Social inclusion'), ('migration', 'Migration'), ('communities', 'Communities'), ('urban_development', 'Urban development'), ('education', 'Education')], help_text='Choose 1-2 topics that describe your idea. Your answer to this question does not influence the selection process. It helps us to get a better overview of the proposals we receive.', max_length=255, verbose_name='Topic'),
        ),
        migrations.AlterField(
            model_name='ideasketcharchived',
            name='importance',
            field=models.TextField(help_text='What motivates you to bring this idea to life? What is your story? What is your connection and mission behind the idea? (max. 800 characters)', max_length=800, verbose_name='Why is this idea important to you?'),
        ),
        migrations.AlterField(
            model_name='ideasketcharchived',
            name='members',
            field=models.TextField(help_text='Please introduce us to the main members of your project team and briefly summarise their experience and skills. (max. 800 characters)', max_length=800, verbose_name='Who is in your project team?'),
        ),
        migrations.AlterField(
            model_name='ideasketcharchived',
            name='outcome',
            field=models.TextField(help_text='If your idea is selected, what will be different a year from now? What will have changed? (max. 800 characters)', max_length=800, verbose_name='What would be a successful outcome for your idea?'),
        ),
        migrations.AlterField(
            model_name='ideasketcharchived',
            name='plan',
            field=models.TextField(help_text='Describe as concretely as possible the approach and/or the method you will use when implementing your idea. What are the steps you plan to take? (max. 800 characters)', max_length=800, verbose_name='How do you plan to get there?'),
        ),
        migrations.AlterField(
            model_name='ideasketcharchived',
            name='reach_out',
            field=models.TextField(blank=True, help_text='What kind of advice, comments or feedback would you like to receive about your idea from others on the platform? (max. 300 characters)', max_length=300, verbose_name='Reach out – get feedback, ideas and inspiration from the Advocate Europe online Community!'),
        ),
        migrations.AlterField(
            model_name='ideasketcharchived',
            name='target_group',
            field=models.TextField(help_text='Which target groups, stakeholders, beneficiaries or audiences are at the centre of your idea? (max. 800 characters)', max_length=800, verbose_name='Who are you doing it for and/or with?'),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='selection_apart',
            field=models.TextField(help_text='What is surprising or unconventional about your idea? What is special about it? (max. 800 characters)', max_length=500, verbose_name='What makes your idea stand apart?'),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='selection_cohesion',
            field=models.TextField(blank=True, max_length=500, verbose_name='How will your idea strengthen connection and cohesion in Europe?'),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='selection_relevance',
            field=models.TextField(blank=True, help_text='How will your project connect to, or influence, people’s daily lives?', max_length=500, verbose_name='What is the practical relevance of your idea to people’s everyday lives?'),
        ),
    ]
