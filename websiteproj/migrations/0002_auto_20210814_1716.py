# Generated by Django 3.2.5 on 2021-08-14 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteproj', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_of_ocean',
            name='dob',
            field=models.DateField(verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='user_of_ocean',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='user_of_ocean',
            name='password',
            field=models.CharField(max_length=100, verbose_name='Password'),
        ),
        migrations.AlterField(
            model_name='user_of_ocean',
            name='uname',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Username'),
        ),
    ]
