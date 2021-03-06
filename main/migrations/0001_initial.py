# Generated by Django 3.1.2 on 2020-10-18 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.TextField()),
                ('education', models.TextField()),
                ('experience', models.CharField(max_length=255)),
                ('industry', models.CharField(max_length=255)),
                ('jobdescription', models.TextField()),
                ('jobid', models.CharField(max_length=255)),
                ('joblocation_address', models.TextField()),
                ('jobtitle', models.CharField(max_length=255)),
                ('numberofpositions', models.CharField(max_length=255)),
                ('payrate', models.CharField(max_length=255)),
                ('postdate', models.CharField(max_length=255)),
                ('site_name', models.CharField(max_length=255)),
                ('skills', models.CharField(max_length=255)),
                ('uniq_id', models.CharField(max_length=255)),
            ],
        ),
    ]
