# Generated by Django 5.1.1 on 2024-09-29 03:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=255, verbose_name='رنگ')),
                ('size', models.CharField(max_length=255, verbose_name='سایز')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.productcategory', verbose_name='دسته بندی'),
        ),
        migrations.AddField(
            model_name='product',
            name='information',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_information', to='products.productinformation', verbose_name='اطلاعات تکمیلی'),
        ),
    ]
