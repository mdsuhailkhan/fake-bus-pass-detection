# Generated by Django 4.1.3 on 2022-12-09 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0009_newpass_qr_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='newpass',
            name='validity',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
