# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-20 17:35
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('searchlist', '0013_auto_20170728_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='city',
            field=models.CharField(default='Seattle', max_length=256),
        ),
        migrations.AlterField(
            model_name='resource',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='main_category',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('CR', 'Crisis'), ('AD', 'Addiction'), ('CH', 'Childcare'), ('YS', 'Youth Services'), ('VE', 'Veteran'), ('RE', 'Rehabilitation'), ('MP', 'Mental/Physical Disability'), ('ED', 'Education'), ('EM', 'Employment'), ('FI', 'Finances'), ('SU', 'Clothing/Housewares'), ('FO', 'Food'), ('HC', 'Healthcare'), ('SH', 'Shelter'), ('LE', 'Legal'), ('ID', 'Identification'), ('SP', 'Spiritual')], max_length=50),
        ),
        migrations.AlterField(
            model_name='resource',
            name='state',
            field=localflavor.us.models.USStateField(default='WA', max_length=2),
        ),
    ]