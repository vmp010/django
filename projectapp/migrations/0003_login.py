# Generated by Django 4.2.6 on 2023-12-13 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0002_categoryr_recorde_recordr_rename_category_categorye_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cName', models.CharField(max_length=8)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
