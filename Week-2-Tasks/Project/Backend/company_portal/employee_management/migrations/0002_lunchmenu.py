# Generated by Django 5.0.7 on 2024-07-24 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LunchMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'LunchMenu',
            },
        ),
    ]