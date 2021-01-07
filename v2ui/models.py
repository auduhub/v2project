# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import django.utils.timezone as timezone
import datetime

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(unique=True, max_length=200, default="")
    user_pass = models.CharField(max_length=200, default="")
    user_email = models.CharField(max_length=200, default="")
    user_contact_type = models.CharField(max_length=200, default="")
    user_contact_num = models.CharField(max_length=200, default="")
    user_reg_date = models.DateTimeField(blank=True)

    class Meta:
        managed = True
        db_table = 'user'

class Line(models.Model):
    line_id = models.IntegerField(unique=True)
    line_remark = models.CharField(max_length=200)
    line_port = models.IntegerField(default=0)
    line_uuid = models.CharField(max_length=200,default="")
    line_expire_date = models.DateTimeField(blank=True)
    line_enable = models.IntegerField(default=0)
    line_transfer = models.BigIntegerField(default=0)
    line_server_domain = models.CharField(max_length=200, default="")
    line_user_id = models.IntegerField()
    line_device_limit = models.IntegerField( default=0)
    line_device_num = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'line'


class Money(models.Model):
    user_id = models.IntegerField(primary_key=True,unique=True)
    money_total = models.IntegerField(default=0)
    money_left = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'money'


class Server(models.Model):
    server_id = models.IntegerField(unique=True)
    server_ip = models.CharField(max_length=200, default="")
    server_domain = models.CharField(max_length=200, default="")
    server_location = models.CharField(max_length=200, default="")
    server_line_num = models.IntegerField(default=0)
    server_line_max = models.IntegerField(default=0)
    server_tag = models.CharField(max_length=200, default="")
    server_load = models.CharField(max_length=200, default="")
    server_speed = models.CharField(max_length=200, default="")
    server_transfer = models.BigIntegerField( default=0)

    class Meta:
        managed = True
        db_table = 'server'



