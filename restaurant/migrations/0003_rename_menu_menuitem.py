# Generated by Django 4.1.5 on 2023-01-28 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0002_menu_inventory"),
    ]

    operations = [
        migrations.RenameModel(old_name="Menu", new_name="MenuItem",),
    ]
