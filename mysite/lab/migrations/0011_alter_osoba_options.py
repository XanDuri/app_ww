# Generated by Django 4.2.16 on 2024-10-17 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0010_alter_osoba_data_dodania'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='osoba',
            options={'ordering': ['nazwisko']},
        ),
    ]
