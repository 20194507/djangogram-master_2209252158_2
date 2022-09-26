# Generated by Django 3.2.13 on 2022-07-21 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20220719_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='cooking_time',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='image_01',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='image_02',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
