# Generated by Django 4.2.6 on 2024-01-02 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0016_alter_depositgoal_goal_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depositgoal',
            name='goal_amount',
            field=models.IntegerField(),
        ),
    ]
