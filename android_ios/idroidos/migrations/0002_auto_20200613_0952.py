# Generated by Django 3.0.3 on 2020-06-13 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('idroidos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comparisoncomment',
            old_name='smartphone',
            new_name='comparison',
        ),
        migrations.RenameField(
            model_name='newscomment',
            old_name='smartphone',
            new_name='news',
        ),
    ]