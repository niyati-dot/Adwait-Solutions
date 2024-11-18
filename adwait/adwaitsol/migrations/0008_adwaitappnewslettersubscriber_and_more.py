# Generated by Django 5.0.7 on 2024-10-03 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adwaitsol', '0007_adwaitappnewslettersubscribe_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdwaitappNewsletterSubscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('subscribed_on', models.DateTimeField()),
            ],
            options={
                'db_table': 'adwaitapp_newslettersubscriber',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='AdwaitappNewsletterSubscribe',
        ),
    ]