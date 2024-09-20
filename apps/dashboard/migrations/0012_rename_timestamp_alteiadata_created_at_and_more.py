# Generated by Django 4.0.5 on 2024-02-22 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0011_training_arrondissement'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alteiadata',
            old_name='timestamp',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='beninyield',
            old_name='timestamp',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='communesatellite',
            old_name='timestamp',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='deptsatellite',
            old_name='timestamp',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='districtsatellite',
            old_name='timestamp',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='nursery',
            old_name='timestamp',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='nurseryplantshistory',
            old_name='timestamp',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='plantation',
            old_name='timestamp',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='specialtuple',
            old_name='timestamp',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='trainer',
            old_name='timestamp',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='training',
            old_name='timestamp',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='trainingmodule',
            old_name='timestamp',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='alteiadata',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='alteia_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='alteiadata',
            name='data_source',
            field=models.CharField(default='TNS/BeninCaju 2020', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alteiadata',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='alteiadata',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='alteia_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='beninyield',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='benin_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='beninyield',
            name='data_source',
            field=models.CharField(default='TNS/BeninCaju 2020', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='beninyield',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='beninyield',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='benin_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='communesatellite',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='commune_satellite_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='communesatellite',
            name='data_source',
            field=models.CharField(default='TNS/BeninCaju 2020', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='communesatellite',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='communesatellite',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='commune_satellite_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='deptsatellite',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='dept_satellite_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='deptsatellite',
            name='data_source',
            field=models.CharField(default='TNS/BeninCaju 2020', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deptsatellite',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='deptsatellite',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='dept_satellite_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='districtsatellite',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='district_satellite_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='districtsatellite',
            name='data_source',
            field=models.CharField(default='TNS/BeninCaju 2020', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='districtsatellite',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='districtsatellite',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='district_satellite_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mothertree',
            name='data_source',
            field=models.CharField(default='TNS/BeninCaju 2020', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nursery',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='nursery_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='nursery',
            name='data_source',
            field=models.CharField(default='TNS/BeninCaju 2020', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nursery',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='nursery',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='nursery_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='nurseryplantshistory',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='nursery_plant_history_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='nurseryplantshistory',
            name='data_source',
            field=models.CharField(default='TNS/BeninCaju 2020', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nurseryplantshistory',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='nurseryplantshistory',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='nursery_plant_history_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='plantation',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='plantation_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='plantation',
            name='data_source',
            field=models.CharField(default='TNS/BeninCaju 2020', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plantation',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='plantation',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='plantation_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='specialtuple',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='special_tuple_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='specialtuple',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='specialtuple',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='special_tuple_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='trainer',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='trainer_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='trainer',
            name='data_source',
            field=models.CharField(default='TNS/BeninCaju 2020', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='trainer',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='trainer_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='training',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='training_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='training',
            name='data_source',
            field=models.CharField(default='TNS/BeninCaju 2020', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='training',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='training',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='training_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='trainingmodule',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='training_module_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='trainingmodule',
            name='data_source',
            field=models.CharField(default='TNS/BeninCaju 2020', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainingmodule',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='trainingmodule',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='training_module_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='nursery',
            name='altitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nursery',
            name='current_area',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nursery',
            name='partner',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]