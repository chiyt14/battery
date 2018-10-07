# Generated by Django 2.1.1 on 2018-10-05 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0007_auto_20181005_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celltestrealdatatable',
            name='sTc0',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Tc0通讯状态'),
        ),
        migrations.AlterField(
            model_name='celltestrealdatatable',
            name='sTc1',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Tc1通讯状态'),
        ),
        migrations.AlterField(
            model_name='celltestrealdatatable',
            name='sTc2',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Tc2通讯状态'),
        ),
        migrations.AlterField(
            model_name='celltestrealdatatable',
            name='sTc3',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Tc3通讯状态'),
        ),
    ]
