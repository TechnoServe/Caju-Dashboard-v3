# Generated by Django 4.2.6 on 2023-10-26 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0007_remove_remorganization_country_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="remuseraccessrequest",
            name="comment",
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
