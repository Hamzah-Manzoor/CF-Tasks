# Generated by Django 5.0.7 on 2024-07-25 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_management', '0004_leavestaken_delete_leaves'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='leaves_taken',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='total_annual_leaves',
        ),
        migrations.AddField(
            model_name='employees',
            name='annual_leaves_taken',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='employees',
            name='casual_leaves_taken',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='employees',
            name='medical_leaves_taken',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='employees',
            name='unpaid_leaves_taken',
            field=models.IntegerField(default=0),
        ),
    ]