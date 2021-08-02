# Generated by Django 3.1.5 on 2021-08-02 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0002_auto_20210802_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='father_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='mobile_number',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='pin',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='state',
            field=models.CharField(max_length=50),
        ),
    ]
