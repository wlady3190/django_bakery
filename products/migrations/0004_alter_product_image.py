# Generated by Django 4.1 on 2023-09-05 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default_cake.jpg', upload_to='products'),
        ),
    ]
