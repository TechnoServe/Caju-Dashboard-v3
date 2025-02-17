# Generated by Django 4.0.5 on 2023-05-19 16:15

import apps.authentication.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0006_administrativelevel'),
    ]

    operations = [
        migrations.CreateModel(
            name='RemOrganization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=200, unique=True)),
                ('domain', models.CharField(default='', max_length=200, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (0, 'Inactive')], default=1)),
                ('country_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.country')),
            ],
        ),
        migrations.CreateModel(
            name='RemRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(choices=[('TNS-ADMIN', 'Tns-Admin'), ('TNS-STAFF', 'Tns-Staff'), ('GOV-ADMIN', 'Gov-Admin'), ('GOV-STAFF', 'Gov-Staff'), ('OTHER', 'Other')], default='OTHER', max_length=200)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (0, 'Inactive')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='RemUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=64)),
                ('phone', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('country_id', models.ForeignKey(default=apps.authentication.models.get_default_user_countries, on_delete=django.db.models.deletion.CASCADE, to='dashboard.country')),
                ('organization', models.ForeignKey(default=apps.authentication.models.get_default_user_org, on_delete=django.db.models.deletion.CASCADE, to='authentication.remorganization')),
                ('role', models.ForeignKey(default=apps.authentication.models.get_default_user_role, on_delete=django.db.models.deletion.CASCADE, to='authentication.remrole')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
