# Generated by Django 4.2 on 2023-06-14 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_posts_sisid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='sisid',
            field=models.UUIDField(auto_created=True),
        ),
    ]
