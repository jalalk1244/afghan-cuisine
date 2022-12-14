# Generated by Django 3.2.16 on 2022-12-01 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0018_alter_reservation_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation_table', to='reservation.table'),
        ),
        migrations.AlterField(
            model_name='table',
            name='Name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
