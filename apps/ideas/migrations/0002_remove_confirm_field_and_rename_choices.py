# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_europe_ideas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ideacomplete',
            name='confirm',
        ),
        migrations.RemoveField(
            model_name='ideasketch',
            name='confirm',
        ),
        migrations.AlterField(
            model_name='ideacomplete',
            name='how_did_you_hear',
            field=models.CharField(verbose_name='How did you hear about Advocate Europe?', choices=[('personal_contact', 'Personal contact'), ('websites', 'Websites'), ('facebook', 'Facebook'), ('twitter', 'Twitter'), ('newsletter', 'Newsletter'), ('other', 'Other')], max_length=2),
        ),
        migrations.AlterField(
            model_name='ideacomplete',
            name='idea_location',
            field=models.CharField(help_text='Please indicate the location of your project. Choose all options that apply.', choices=[('city', 'City, country or region'), ('online', 'Online'), ('ruhr_linkage', 'Linkage to the Ruhr area of Germany')], max_length=250),
        ),
        migrations.AlterField(
            model_name='ideacomplete',
            name='idea_topics',
            field=models.CharField(choices=[('democracy_participation', 'Democracy and participation'), ('arts_cultural_activities', 'Arts and (inter-)cultural activities'), ('environment', 'Environment'), ('social_inclusion', 'Social inclusion'), ('migration', 'Migration'), ('communities', 'Communities'), ('urban_development', 'Urban development'), ('education', 'Education')], max_length=2),
        ),
        migrations.AlterField(
            model_name='ideacomplete',
            name='organisation_status',
            field=models.CharField(choices=[('non_profit', 'I am applying on behalf of a registered non-profit organisation, e.g. NGO'), ('non_profit_planned', 'Registration as a non-profit organisation is planned or is already underway'), ('no_non_profit', 'I have a really good idea, but will need help to register a non-profit organisation'), ('other', 'Other')], max_length=2),
        ),
        migrations.AlterField(
            model_name='ideasketch',
            name='collaboration_camp_option',
            field=models.CharField(help_text='Choose one of the following options. More information about the two tracks is available here: (Link).', choices=[('single_track', 'Single track'), ('partner_track', 'Partner track'), ('not_sure', "I'm not sure yet")], max_length=2),
        ),
        migrations.AlterField(
            model_name='ideasketch',
            name='how_did_you_hear',
            field=models.CharField(verbose_name='How did you hear about Advocate Europe?', choices=[('personal_contact', 'Personal contact'), ('websites', 'Websites'), ('facebook', 'Facebook'), ('twitter', 'Twitter'), ('newsletter', 'Newsletter'), ('other', 'Other')], max_length=2),
        ),
        migrations.AlterField(
            model_name='ideasketch',
            name='idea_location',
            field=models.CharField(help_text='Please indicate the location of your project. Choose all options that apply.', choices=[('city', 'City, country or region'), ('online', 'Online'), ('ruhr_linkage', 'Linkage to the Ruhr area of Germany')], max_length=250),
        ),
        migrations.AlterField(
            model_name='ideasketch',
            name='idea_topics',
            field=models.CharField(choices=[('democracy_participation', 'Democracy and participation'), ('arts_cultural_activities', 'Arts and (inter-)cultural activities'), ('environment', 'Environment'), ('social_inclusion', 'Social inclusion'), ('migration', 'Migration'), ('communities', 'Communities'), ('urban_development', 'Urban development'), ('education', 'Education')], max_length=2),
        ),
        migrations.AlterField(
            model_name='ideasketch',
            name='organisation_status',
            field=models.CharField(choices=[('non_profit', 'I am applying on behalf of a registered non-profit organisation, e.g. NGO'), ('non_profit_planned', 'Registration as a non-profit organisation is planned or is already underway'), ('no_non_profit', 'I have a really good idea, but will need help to register a non-profit organisation'), ('other', 'Other')], max_length=2),
        ),
    ]
