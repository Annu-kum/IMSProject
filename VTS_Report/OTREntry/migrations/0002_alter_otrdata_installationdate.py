# Generated by Django 5.0.2 on 2024-08-06 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OTREntry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otrdata',
            name='InstallationDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
