# Generated by Django 3.1.4 on 2020-12-22 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplicant',
            name='applicant_email_id',
            field=models.EmailField(default='Not Disclosed', max_length=254),
        ),
    ]
