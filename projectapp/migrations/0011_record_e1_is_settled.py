# Generated by Django 4.2.6 on 2023-12-26 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0010_alter_record_e1_user_alter_record_r1_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='record_e1',
            name='is_settled',
            field=models.BooleanField(default=False),
        ),
    ]