# Generated by Django 2.1.5 on 2020-10-29 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='username',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
