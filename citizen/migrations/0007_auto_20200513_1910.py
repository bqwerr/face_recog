# Generated by Django 3.0.5 on 2020-05-13 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citizen', '0006_auto_20200513_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citizen',
            name='dob',
            field=models.DateTimeField(max_length=8, null=True),
        ),
    ]
