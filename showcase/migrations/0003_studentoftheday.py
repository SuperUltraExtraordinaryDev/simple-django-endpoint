# Generated by Django 3.0.1 on 2019-12-19 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0002_auto_20191212_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentOfTheDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='showcase.Profile')),
            ],
        ),
    ]