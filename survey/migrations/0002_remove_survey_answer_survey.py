# Generated by Django 2.2 on 2021-01-22 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey_answer',
            name='survey',
        ),
    ]
