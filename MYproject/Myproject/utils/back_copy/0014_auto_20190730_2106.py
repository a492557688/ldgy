# Generated by Django 2.2.3 on 2019-07-30 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20190730_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housing_img',
            name='is_first',
            field=models.BooleanField(default=False),
        ),
    ]
