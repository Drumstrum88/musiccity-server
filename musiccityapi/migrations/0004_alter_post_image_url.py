# Generated by Django 4.1.3 on 2024-02-08 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musiccityapi', '0003_alter_postreaction_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_url',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
