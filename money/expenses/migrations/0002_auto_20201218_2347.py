# Generated by Django 3.1.4 on 2020-12-18 20:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='source',
        ),
        migrations.AddField(
            model_name='entry',
            name='responsible_user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='car_to_user', to=settings.AUTH_USER_MODEL, verbose_name='Responsible'),
        ),
        migrations.AddField(
            model_name='entry',
            name='type',
            field=models.CharField(choices=[('income', 'Income'), ('expenses', 'Expenses')], default='expenses', max_length=100, verbose_name='Type'),
        ),
        migrations.DeleteModel(
            name='Source_types',
        ),
    ]
