# Generated by Django 3.1.1 on 2020-09-30 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20200930_1255'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('premium', 'Can read all books')]},
        ),
    ]
