# Generated by Django 4.0 on 2023-06-16 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='tags',
        ),
        migrations.AddField(
            model_name='todoitem',
            name='tags',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]