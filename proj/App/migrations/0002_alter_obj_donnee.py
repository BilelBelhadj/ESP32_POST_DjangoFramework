# Generated by Django 4.1.3 on 2022-12-09 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obj',
            name='donnee',
            field=models.CharField(max_length=100),
        ),
    ]