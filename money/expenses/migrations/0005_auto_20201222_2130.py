# Generated by Django 3.1.4 on 2020-12-22 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0004_auto_20201219_0023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='сategory',
            new_name='category',
        ),
        migrations.AddField(
            model_name='entry',
            name='notes',
            field=models.TextField(blank=True, max_length=100, verbose_name='Notes'),
        ),
        migrations.DeleteModel(
            name='Total',
        ),
    ]