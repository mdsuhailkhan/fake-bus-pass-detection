# Generated by Django 4.1.3 on 2022-12-06 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0007_alter_userfeedback_feedback2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfeedback',
            name='feedback2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.newpass'),
        ),
    ]