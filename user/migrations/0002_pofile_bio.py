# Generated by Django 3.1.1 on 2020-12-05 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pofile',
            name='bio',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
