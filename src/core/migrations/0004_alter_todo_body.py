# Generated by Django 5.0.4 on 2024-05-07 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_todo_desc_todo_body_alter_todo_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='body',
            field=models.TextField(blank=True, default='No description'),
        ),
    ]