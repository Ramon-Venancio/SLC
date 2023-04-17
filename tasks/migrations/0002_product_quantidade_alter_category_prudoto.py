# Generated by Django 4.2 on 2023-04-16 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantidade',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='category',
            name='prudoto',
            field=models.ManyToManyField(blank=True, related_name='categorias', to='tasks.product'),
        ),
    ]
