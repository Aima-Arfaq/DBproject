# Generated by Django 5.1.4 on 2025-01-01 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostelManagement', '0004_alter_menu_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annualduesstatus',
            name='pais',
        ),
        migrations.AddField(
            model_name='annualduesstatus',
            name='paymentStatus',
            field=models.CharField(choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')], default='unpaid', max_length=10),
        ),
    ]
