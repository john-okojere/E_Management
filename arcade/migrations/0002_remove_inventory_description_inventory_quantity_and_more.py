# Generated by Django 5.1.3 on 2024-11-21 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arcade', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='Description',
        ),
        migrations.AddField(
            model_name='inventory',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='inventory',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
