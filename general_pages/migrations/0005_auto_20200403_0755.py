# Generated by Django 3.0.4 on 2020-04-03 07:55

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('general_pages', '0004_contactus_email_sent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default=None, max_length=128, null=True, region=None, unique=True),
        ),
    ]
