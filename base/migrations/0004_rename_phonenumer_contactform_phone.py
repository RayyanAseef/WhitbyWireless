# Generated by Django 4.2.5 on 2023-12-20 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='phoneNumer',
            new_name='phone',
        ),
    ]