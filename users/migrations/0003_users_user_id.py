# Generated by Django 3.2.13 on 2022-06-15 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_users_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='user_id',
            field=models.IntegerField(default=0.4923793262888535),
        ),
    ]