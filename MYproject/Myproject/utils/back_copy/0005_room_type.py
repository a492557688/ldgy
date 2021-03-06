# Generated by Django 2.2.3 on 2019-07-27 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190725_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('is_show', models.BooleanField(default=True)),
                ('is_dele', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=32)),
                ('xuanchuan_img', models.FileField(upload_to='Room_type')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
