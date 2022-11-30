# Generated by Django 3.2.16 on 2022-11-30 08:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0010_alter_reservation_num_of_guest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='num_of_guest',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='table',
            name='max_num_guest',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10)]),
        ),
    ]