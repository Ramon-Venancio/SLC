# Generated by Django 4.2 on 2023-04-17 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_product_quantidade_alter_category_prudoto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='prudoto',
            new_name='prudotos',
        ),
    ]