# Generated by Django 3.1.5 on 2021-08-02 17:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_enrolled',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
