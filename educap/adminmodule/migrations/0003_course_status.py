# Generated by Django 2.1.5 on 2022-06-09 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminmodule', '0002_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.CharField(default='active', max_length=10),
        ),
    ]