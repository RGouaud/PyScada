# Generated by Django 2.2.8 on 2020-11-04 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smbus', '0004_auto_20191004_0912'),
    ]

    operations = [
        migrations.CreateModel(
            name='SMBusDeviceHandler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('handler_class', models.CharField(default='pyscada.smbus.devices.ups_pico', help_text='a Base class to extend can be found at pyscada.smbus.devices.GenericDevice', max_length=255)),
                ('handler_path', models.CharField(blank=True, default=None, max_length=255, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='smbusdevice',
            name='device_type',
        ),
        migrations.AddField(
            model_name='smbusdevice',
            name='instrument',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='smbus.SMBusDeviceHandler'),
        ),
    ]
