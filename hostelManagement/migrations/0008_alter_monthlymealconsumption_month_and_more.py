# Generated by Django 5.1.4 on 2025-01-01 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostelManagement', '0007_alter_monthlymealconsumption_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlymealconsumption',
            name='month',
            field=models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], default='October', max_length=10),
        ),
        migrations.AlterField(
            model_name='monthlymealconsumption',
            name='perDayCharges',
            field=models.DecimalField(decimal_places=2, default=250, max_digits=10),
        ),
    ]
