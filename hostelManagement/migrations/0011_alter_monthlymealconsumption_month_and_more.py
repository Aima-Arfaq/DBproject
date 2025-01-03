# Generated by Django 5.1.4 on 2025-01-01 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostelManagement', '0010_alter_monthlymealconsumption_month_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlymealconsumption',
            name='month',
            field=models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=10),
        ),
        migrations.AlterField(
            model_name='monthlymealconsumption',
            name='perDayCharges',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='monthlymealconsumption',
            name='year',
            field=models.PositiveIntegerField(),
        ),
    ]
