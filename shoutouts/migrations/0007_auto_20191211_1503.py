# Generated by Django 3.0 on 2019-12-11 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoutouts', '0006_shoutout_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoutout',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
