# Generated by Django 3.2.5 on 2021-08-14 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_of_ocean',
            fields=[
                ('uname', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
