# Generated by Django 3.2.16 on 2022-11-30 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0016_auto_20221130_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='email',
            field=models.EmailField(max_length=80),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='phone_num',
            field=models.CharField(max_length=12),
        ),
    ]
