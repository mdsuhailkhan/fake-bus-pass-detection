# Generated by Django 4.1.3 on 2022-12-06 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0005_sentimentanalysis_alter_userfeedback_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentimentanalysis',
            name='senti',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.newpass'),
        ),
    ]