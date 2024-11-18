# Generated by Django 5.0.7 on 2024-08-28 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adwaitsol', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdwaitappMainServices',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('creation_date', models.DateTimeField()),
                ('name', models.CharField(max_length=255)),
                ('dept_id_id', models.BigIntegerField()),
            ],
            options={
                'db_table': 'adwaitapp_main_services',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AdwaitappSubServices',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('main_service_id_id', models.BigIntegerField()),
            ],
            options={
                'db_table': 'adwaitapp_sub_services',
                'managed': False,
            },
        ),
    ]