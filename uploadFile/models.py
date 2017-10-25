# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class RawdataCapa2(models.Model):
    timestamp = models.DateTimeField(db_column='TIMESTAMP', primary_key=True)  # Field name made lowercase.
    t0 = models.DecimalField(db_column='T0', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    t10 = models.DecimalField(db_column='T10', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    t30 = models.DecimalField(db_column='T30', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    t50 = models.DecimalField(db_column='T50', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    t150 = models.DecimalField(db_column='T150', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sf10 = models.DecimalField(db_column='SF10', max_digits=3, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    sf30 = models.DecimalField(db_column='SF30', max_digits=3, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    sf50 = models.DecimalField(db_column='SF50', max_digits=3, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    sf70 = models.DecimalField(db_column='SF70', max_digits=3, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    sf90 = models.DecimalField(db_column='SF90', max_digits=3, decimal_places=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RAWDATA_Capa2'


class RawdataCapa3(models.Model):
    timestamp = models.DateTimeField(db_column='TIMESTAMP', primary_key=True)  # Field name made lowercase.
    t0 = models.DecimalField(db_column='T0', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    t10 = models.DecimalField(db_column='T10', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    t30 = models.DecimalField(db_column='T30', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    t50 = models.DecimalField(db_column='T50', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sf10 = models.DecimalField(db_column='SF10', max_digits=3, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    sf30 = models.DecimalField(db_column='SF30', max_digits=3, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    sf50 = models.DecimalField(db_column='SF50', max_digits=3, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    sf70 = models.DecimalField(db_column='SF70', max_digits=3, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    sf90 = models.DecimalField(db_column='SF90', max_digits=3, decimal_places=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RAWDATA_Capa3'


class RawdataCapa4(models.Model):
    timestamp = models.DateTimeField(db_column='TIMESTAMP', primary_key=True)  # Field name made lowercase.
    ws_ms_avg = models.DecimalField(db_column='WS_ms_Avg', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    winddir = models.DecimalField(db_column='WindDir', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    airtc_20_avg = models.DecimalField(db_column='AirTC_20_Avg', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    rh_20 = models.DecimalField(db_column='RH_20', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    airtc_15_avg = models.DecimalField(db_column='AirTC_15_Avg', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    rh_15 = models.DecimalField(db_column='RH_15', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    airtc_10_avg = models.DecimalField(db_column='AirTC_10_Avg', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    rh_10 = models.DecimalField(db_column='RH_10', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    airtc_5_avg = models.DecimalField(db_column='AirTC_5_Avg', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    rh_5 = models.DecimalField(db_column='RH_5', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    nr_wm2_avg = models.DecimalField(db_column='NR_Wm2_Avg', max_digits=9, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    sevolt_avg = models.DecimalField(db_column='SEVolt_Avg', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    temp_c_avg_1_field = models.DecimalField(db_column='Temp_C_Avg(1)', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    temp_c_avg_2_field = models.DecimalField(db_column='Temp_C_Avg(2)', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    temp_c_avg_3_field = models.DecimalField(db_column='Temp_C_Avg(3)', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    temp_c_avg_4_field = models.DecimalField(db_column='Temp_C_Avg(4)', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    temp_c_avg_5_field = models.DecimalField(db_column='Temp_C_Avg(5)', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    temp_c_avg_6_field = models.DecimalField(db_column='Temp_C_Avg(6)', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    result1_avg = models.DecimalField(db_column='Result1_Avg', max_digits=4, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    result2_avg = models.DecimalField(db_column='Result2_Avg', max_digits=4, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    result3_avg = models.DecimalField(db_column='Result3_Avg', max_digits=4, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    result4_avg = models.DecimalField(db_column='Result4_Avg', max_digits=4, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    result5_avg = models.DecimalField(db_column='Result5_Avg', max_digits=4, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    inf_data = models.DecimalField(db_column='Inf_data', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    temp_c_avg_7_field = models.DecimalField(db_column='Temp_C_Avg(7)', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    rain_mm_tot = models.DecimalField(db_column='Rain_mm_Tot', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pressure_avg = models.DecimalField(db_column='Pressure_Avg', max_digits=8, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RAWDATA_Capa4'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
