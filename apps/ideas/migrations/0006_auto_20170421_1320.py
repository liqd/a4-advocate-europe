# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocate_europe_ideas', '0005_auto_20170421_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='ideacomplete',
            name='members',
            field=models.TextField(help_text='Please introduce us to the main members of your project team and briefly summariese their experience and skills. (max. 500 characters)', max_length=500, verbose_name='Who is in your project team?', default='many members and all their info'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ideasketch',
            name='members',
            field=models.TextField(help_text='Please introduce us to the main members of your project team and briefly summariese their experience and skills. (max. 500 characters)', max_length=500, verbose_name='Who is in your project team?', default='many members and all their info'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ideacomplete',
            name='collaborators_emails',
            field=models.TextField(help_text='Here you can insert the email addresses of up to 5 collaborators. Each of the named collaborators will receive an email inviting them to register on the Advocate Europe website. After registering they will appear with their user name on your idea page and will be able to edit your idea. ', max_length=200, verbose_name='Please add your collaborators here.'),
        ),
        migrations.AlterField(
            model_name='ideacomplete',
            name='idea_location_ruhr',
            field=models.TextField(help_text='If you selected Ruhr area, please explain. Is your project connected to the Ruhr area of Germany through project partners, audiences, or in some other way? Please provide further details. (max. 200 characters)', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='ideacomplete',
            name='idea_location_specify',
            field=models.TextField(help_text='Please specify the city, country and region, e.g. Berlin, Germany', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='ideacomplete',
            name='organisation_status_extra',
            field=models.TextField(help_text='If you selected other, please clarify your current status. How can we help you? (max. 200 characters)', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='ideacomplete',
            name='partners_more_info',
            field=models.TextField(help_text='Please use this field if you have more than 3 partner organisations or if you want to tell us more about your proposed partnership arrangements (max. 200 characters).', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='ideasketch',
            name='collaborators_emails',
            field=models.TextField(help_text='Here you can insert the email addresses of up to 5 collaborators. Each of the named collaborators will receive an email inviting them to register on the Advocate Europe website. After registering they will appear with their user name on your idea page and will be able to edit your idea. ', max_length=200, verbose_name='Please add your collaborators here.'),
        ),
        migrations.AlterField(
            model_name='ideasketch',
            name='idea_location_ruhr',
            field=models.TextField(help_text='If you selected Ruhr area, please explain. Is your project connected to the Ruhr area of Germany through project partners, audiences, or in some other way? Please provide further details. (max. 200 characters)', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='ideasketch',
            name='idea_location_specify',
            field=models.TextField(help_text='Please specify the city, country and region, e.g. Berlin, Germany', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='ideasketch',
            name='organisation_status_extra',
            field=models.TextField(help_text='If you selected other, please clarify your current status. How can we help you? (max. 200 characters)', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='ideasketch',
            name='partners_more_info',
            field=models.TextField(help_text='Please use this field if you have more than 3 partner organisations or if you want to tell us more about your proposed partnership arrangements (max. 200 characters).', max_length=200, blank=True),
        ),
    ]
