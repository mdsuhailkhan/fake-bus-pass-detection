# Generated by Django 4.1.3 on 2022-12-07 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0008_alter_userfeedback_feedback2'),
    ]

    operations = [
        migrations.AddField(
            model_name='newpass',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
