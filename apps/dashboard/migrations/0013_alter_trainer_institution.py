# Generated by Django 4.0.5 on 2024-02-22 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_rename_timestamp_alteiadata_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='institution',
            field=models.CharField(max_length=200),
        ),
    ]
