# Generated by Django 3.0.3 on 2020-05-03 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smc_app', '0002_userprofileinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatdata',
            name='ctype',
            field=models.CharField(default='T', max_length=1),
        ),
    ]
