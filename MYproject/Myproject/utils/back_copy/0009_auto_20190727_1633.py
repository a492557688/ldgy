# Generated by Django 2.2.3 on 2019-07-27 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_room_type_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('is_show', models.BooleanField(default=True)),
                ('is_dele', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=257)),
                ('content', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Housing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('is_show', models.BooleanField(default=True)),
                ('is_dele', models.BooleanField(default=False)),
                ('room_id', models.CharField(max_length=15)),
                ('xianjia', models.IntegerField()),
                ('hot', models.IntegerField()),
                ('xiaoqu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Housing_estate')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Kuaixun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('is_show', models.BooleanField(default=True)),
                ('is_dele', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('kuaixun_img', models.CharField(max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('is_show', models.BooleanField(default=True)),
                ('is_dele', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=32)),
                ('hot', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Zhoubian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('is_show', models.BooleanField(default=True)),
                ('is_dele', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Housing_img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('is_show', models.BooleanField(default=True)),
                ('is_dele', models.BooleanField(default=False)),
                ('img_url', models.CharField(max_length=256)),
                ('the_hourse', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.Housing')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='housing',
            name='zhoubian',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.Zhoubian'),
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('is_show', models.BooleanField(default=True)),
                ('is_dele', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=256)),
                ('room', models.ManyToManyField(to='home.Housing')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='housing_estate',
            name='xiaozheng',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Town'),
        ),
        migrations.AddField(
            model_name='housing_estate',
            name='zhoubian',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Zhoubian'),
        ),
    ]
