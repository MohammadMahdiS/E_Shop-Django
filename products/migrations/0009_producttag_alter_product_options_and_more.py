# Generated by Django 5.1.1 on 2024-09-29 04:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_productinformation_alter_product_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=255, verbose_name='تگ')),
            ],
            options={
                'verbose_name': 'تگ',
                'verbose_name_plural': 'تگ ها',
            },
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'محصول', 'verbose_name_plural': 'محصولات'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'دسته بندی محصول', 'verbose_name_plural': 'دسته بندی های محصول'},
        ),
        migrations.AlterModelOptions(
            name='productinformation',
            options={'verbose_name': 'اطلاعات تکمیلی محصول', 'verbose_name_plural': 'تمامی اطلاعات تکمیلی'},
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='products.productcategory', verbose_name='دسته بندی'),
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(related_name='product_tag', to='products.producttag', verbose_name='تگ'),
        ),
    ]
