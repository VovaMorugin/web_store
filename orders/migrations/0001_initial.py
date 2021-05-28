# Generated by Django 3.2.3 on 2021-05-28 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('time_checkout', models.DateTimeField(blank=True, null=True, verbose_name='Time of checkout')),
                ('time_delivery', models.DateTimeField(blank=True, null=True, verbose_name='Time of delivery')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer', verbose_name='Customer')),
                ('customer_shipping_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.customeraddress', verbose_name='Shipping address')),
                ('promocode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.promocode')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='Quantity')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Price')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'order_product',
                'verbose_name_plural': 'order_products',
                'db_table': 'order_products',
            },
        ),
    ]