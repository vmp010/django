# Generated by Django 4.2.6 on 2023-12-13 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0003_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='regist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cName', models.CharField(max_length=8)),
                ('cEmail', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]