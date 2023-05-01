# Generated by Django 4.2 on 2023-04-29 20:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('middle_class_check', '0003_alter_medianhouseholdincome_geography_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medianhouseholdincome',
            name='geography_code',
            field=models.CharField(max_length=2, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]