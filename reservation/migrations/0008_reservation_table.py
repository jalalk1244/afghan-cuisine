# Generated by Django 3.2.16 on 2022-11-30 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0007_reservation_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='table',
            field=models.ForeignKey(default='Table', on_delete=django.db.models.deletion.CASCADE, related_name='reservation_table', to='reservation.table', to_field='Name'),
        ),
    ]
