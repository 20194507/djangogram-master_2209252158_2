# Generated by Django 3.2.13 on 2022-07-28 14:19

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_post_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
        ),
    ]