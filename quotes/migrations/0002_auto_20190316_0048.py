# Generated by Django 2.1.7 on 2019-03-15 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personality',
            options={'verbose_name_plural': 'personalities'},
        ),
        migrations.AlterField(
            model_name='personality',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
    ]
