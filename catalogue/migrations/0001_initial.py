# Generated by Django 2.1 on 2018-08-20 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('manufacturer', models.CharField(max_length=120)),
                ('category', models.CharField(max_length=120)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]