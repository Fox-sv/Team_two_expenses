# Generated by Django 3.1.4 on 2020-12-18 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_auto_20201218_2347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='type',
            new_name='type_inc_exp',
        ),
    ]
