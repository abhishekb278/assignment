# Generated by Django 3.0.3 on 2021-03-02 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(null=True, verbose_name='phone'),
        ),
    ]
