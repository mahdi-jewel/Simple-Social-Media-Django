# Generated by Django 3.0.3 on 2020-06-22 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0002_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='fuu_name',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]