# Generated by Django 4.2rc1 on 2023-03-30 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hmi', '0070_move_displayvalueoptions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='displayvalueoption',
            name='color_1',
        ),
        migrations.RemoveField(
            model_name='displayvalueoption',
            name='color_2',
        ),
        migrations.RemoveField(
            model_name='displayvalueoption',
            name='color_3',
        ),
        migrations.RemoveField(
            model_name='displayvalueoption',
            name='color_level_1',
        ),
        migrations.RemoveField(
            model_name='displayvalueoption',
            name='color_level_1_type',
        ),
        migrations.RemoveField(
            model_name='displayvalueoption',
            name='color_level_2',
        ),
        migrations.RemoveField(
            model_name='displayvalueoption',
            name='color_level_2_type',
        ),
        migrations.RemoveField(
            model_name='displayvalueoption',
            name='color_type',
        ),
        migrations.RemoveField(
            model_name='displayvalueoption',
            name='mode',
        ),
    ]
