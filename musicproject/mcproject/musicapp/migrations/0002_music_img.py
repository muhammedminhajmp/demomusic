# Generated by Django 3.2.16 on 2022-10-28 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='img',
            field=models.ImageField(default='dfgh', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
