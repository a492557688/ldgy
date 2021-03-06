# Generated by Django 2.2.3 on 2019-07-25 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190725_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='is_dele',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='area',
            name='is_show',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='banner',
            name='is_dele',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='banner',
            name='is_show',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='housing_estate',
            name='is_dele',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='housing_estate',
            name='is_show',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='nav',
            name='is_dele',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='nav',
            name='is_show',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='nav_title',
            name='is_dele',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='nav_title',
            name='is_show',
            field=models.BooleanField(default=True),
        ),
    ]
