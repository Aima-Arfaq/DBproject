# Generated by Django 5.1.4 on 2025-01-02 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostelManagement', '0004_alter_menu_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlyduesstatus',
            name='month',
            field=models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], default='October', max_length=10),
        ),
        migrations.AlterField(
            model_name='monthlyduesstatus',
            name='payment_status',
            field=models.CharField(choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')], default='paid', max_length=7),
        ),
        migrations.AlterField(
            model_name='monthlyduesstatus',
            name='year',
            field=models.PositiveIntegerField(default=2024),
        ),
    ]
