# Generated by Django 3.2.3 on 2021-08-04 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20210804_2239'),
        ('products', '0003_auto_20210616_0517'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Promocode',
        ),
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name': 'Brand', 'verbose_name_plural': 'Brands'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'Product to category', 'verbose_name_plural': 'Products to categories'},
        ),
        migrations.AlterModelOptions(
            name='productreview',
            options={'verbose_name': 'Review', 'verbose_name_plural': 'Reviews'},
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.brand', verbose_name='Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='Old price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Photo'),
        ),
        migrations.AlterModelTable(
            name='productcategory',
            table='products_categories',
        ),
        migrations.AlterModelTable(
            name='productreview',
            table='products_reviews',
        ),
    ]
