# Generated by Django 2.2.3 on 2019-08-03 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='housing',
            name='level',
            field=models.CharField(default='2/7曾', max_length=64),
            preserve_default=False,
        ),
    ]
