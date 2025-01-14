# Generated by Django 4.0.5 on 2023-05-25 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_country_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='level0_field',
            field=models.CharField(default='NAME_0', max_length=200),
        ),
        migrations.AddField(
            model_name='country',
            name='level0_name',
            field=models.CharField(default='Country', max_length=200),
        ),
        migrations.AddField(
            model_name='country',
            name='level1_field',
            field=models.CharField(default='NAME_1', max_length=200),
        ),
        migrations.AddField(
            model_name='country',
            name='level1_name',
            field=models.CharField(default='Department', max_length=200),
        ),
        migrations.AddField(
            model_name='country',
            name='level2_field',
            field=models.CharField(default='NAME_2', max_length=200),
        ),
        migrations.AddField(
            model_name='country',
            name='level2_name',
            field=models.CharField(default='Commune', max_length=200),
        ),
        migrations.AddField(
            model_name='country',
            name='level3_field',
            field=models.CharField(default='NAME_3', max_length=200),
        ),
        migrations.AddField(
            model_name='country',
            name='level3_name',
            field=models.CharField(default='District', max_length=200),
        ),
    ]
