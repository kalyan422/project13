# Generated by Django 4.2.2 on 2023-06-13 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('jobid', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('skills', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
    ]
