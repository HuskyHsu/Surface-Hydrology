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
    receivedate = models.DateField(db_column='ReceiveDate')  # Field name made lowercase.

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
    receivedate = models.DateField(db_column='ReceiveDate')  # Field name made lowercase.

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
    temp_c_avg_1 = models.DecimalField(db_column='Temp_C_Avg_1', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    temp_c_avg_2 = models.DecimalField(db_column='Temp_C_Avg_2', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    temp_c_avg_3 = models.DecimalField(db_column='Temp_C_Avg_3', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    temp_c_avg_4 = models.DecimalField(db_column='Temp_C_Avg_4', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    temp_c_avg_5 = models.DecimalField(db_column='Temp_C_Avg_5', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    temp_c_avg_6 = models.DecimalField(db_column='Temp_C_Avg_6', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    result1_avg = models.DecimalField(db_column='Result1_Avg', max_digits=4, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    result2_avg = models.DecimalField(db_column='Result2_Avg', max_digits=4, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    result3_avg = models.DecimalField(db_column='Result3_Avg', max_digits=4, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    result4_avg = models.DecimalField(db_column='Result4_Avg', max_digits=4, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    result5_avg = models.DecimalField(db_column='Result5_Avg', max_digits=4, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    inf_data = models.DecimalField(db_column='Inf_data', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    temp_c_avg_7 = models.DecimalField(db_column='Temp_C_Avg_7', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    rain_mm_tot = models.DecimalField(db_column='Rain_mm_Tot', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pressure_avg = models.DecimalField(db_column='Pressure_Avg', max_digits=8, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    receivedate = models.DateField(db_column='ReceiveDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RAWDATA_Capa4'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Members(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    master_graduation_year = models.IntegerField(blank=True, null=True)
    master_disseration_title = models.CharField(max_length=100, blank=True, null=True)
    master_disseration_url = models.CharField(max_length=150, blank=True, null=True)
    doctor_graduation_year = models.IntegerField(blank=True, null=True)
    doctor_disseration_title = models.CharField(max_length=150, blank=True, null=True)
    doctor_disseration_url = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'members'


class Papers(models.Model):
    pid = models.AutoField(primary_key=True)
    author = models.CharField(max_length=200)
    date = models.CharField(max_length=7)
    title = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'papers'


class Plans(models.Model):
    pid = models.AutoField(primary_key=True)
    year = models.IntegerField()
    unit = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=20)
    start_time = models.DateField()
    end_time = models.DateField()

    class Meta:
        managed = False
        db_table = 'plans'


class WorkExperience(models.Model):
    pid = models.AutoField(primary_key=True)
    unit = models.CharField(max_length=50)
    department = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=50)
    start_year = models.IntegerField(db_column='start_Year')  # Field name made lowercase.
    end_year = models.IntegerField(db_column='end_Year', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'work_experience'
