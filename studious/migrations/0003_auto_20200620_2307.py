# Generated by Django 3.0.6 on 2020-06-20 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studious', '0002_org_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmcid', models.IntegerField()),
                ('open_data', models.CharField(max_length=5)),
                ('data_share', models.CharField(max_length=5)),
                ('data_statement', models.TextField()),
                ('edit_user', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='org',
            name='data_score',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='org',
            name='has_three_pubs',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='data_score',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='has_three_pubs',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectpaper',
            name='data_score',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectpaper',
            name='org_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectpaper',
            name='pi_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
