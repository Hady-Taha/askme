# Generated by Django 3.1.1 on 2020-12-06 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
