# Generated by Django 3.2.3 on 2021-07-15 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
