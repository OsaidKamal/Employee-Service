# Generated by Django 3.1.5 on 2021-02-01 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0004_auto_20210131_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
