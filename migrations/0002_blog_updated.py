# Generated by Django 2.0.7 on 2018-07-23 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]