# Generated by Django 5.0.8 on 2024-09-20 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_room_folders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='folders',
            field=models.TextField(blank=True, null=True),
        ),
    ]
