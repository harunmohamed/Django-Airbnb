# Generated by Django 2.2.4 on 2020-04-14 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtor',
            name='email',
            field=models.CharField(default='realtor@email.com', max_length=50),
        ),
    ]
