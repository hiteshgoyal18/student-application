# Generated by Django 3.1.5 on 2021-08-02 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0003_auto_20210802_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]
