# Generated by Django 2.2 on 2020-09-21 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0004_order_status_sales_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_status',
            name='order_recived',
            field=models.CharField(choices=[('D', 'Done'), ('P', 'Pending')], default='D', max_length=2, verbose_name='Order Received'),
        ),
        migrations.AlterField(
            model_name='order_status',
            name='sales_manager',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='procurement.Sales_Manager', verbose_name='Order Code'),
        ),
    ]