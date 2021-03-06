# Generated by Django 3.0.6 on 2020-05-28 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmcid', models.IntegerField()),
                ('doi', models.CharField(max_length=48)),
                ('journal_title', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=250)),
                ('journal_year', models.SmallIntegerField()),
                ('open_data', models.CharField(max_length=5)),
                ('data_share', models.CharField(max_length=5)),
                ('project_id', models.IntegerField()),
                ('contact_pi_project_leader', models.CharField(max_length=50)),
                ('organization_name', models.CharField(max_length=128)),
            ],
            options={
                'ordering': ('-pmcid',),
            },
        ),
    ]
