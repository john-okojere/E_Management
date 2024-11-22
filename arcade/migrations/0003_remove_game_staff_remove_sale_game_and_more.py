# Generated by Django 5.1.3 on 2024-11-22 03:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arcade', '0002_remove_inventory_description_inventory_quantity_and_more'),
        ('shared', '0003_alter_staffprofile_level_alter_staffprofile_role_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='staff',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='game',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='sale_type',
        ),
        migrations.AddField(
            model_name='sale',
            name='total',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=15),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='SaleDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposed_discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('approved', models.BooleanField(default=False)),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sale_approver', to='shared.staffprofile')),
                ('cashier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared.staffprofile')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arcade.sale')),
            ],
        ),
        migrations.CreateModel(
            name='SaleItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arcade.inventory')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='arcade.sale')),
            ],
        ),
        migrations.CreateModel(
            name='SaleItemDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposed_discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('approved', models.BooleanField(default=False)),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='saleitem_approver', to='shared.staffprofile')),
                ('cashier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared.staffprofile')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arcade.saleitem')),
            ],
        ),
        migrations.DeleteModel(
            name='Discount',
        ),
        migrations.DeleteModel(
            name='Game',
        ),
    ]