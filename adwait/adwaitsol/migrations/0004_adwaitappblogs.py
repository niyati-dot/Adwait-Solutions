# Generated by Django 5.0.7 on 2024-08-30 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adwaitsol', '0003_adwaitappinquiries'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdwaitappBlogs',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('creation_date', models.DateTimeField()),
                ('subject', models.CharField(max_length=255)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('tags', models.CharField(blank=True, max_length=255, null=True)),
                ('img', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.SmallIntegerField(blank=True, null=True)),
                ('dept_id_id', models.BigIntegerField()),
                ('main_service_id_id', models.BigIntegerField()),
            ],
            options={
                'db_table': 'adwaitapp_blogs',
                'managed': False,
            },
        ),
    ]
