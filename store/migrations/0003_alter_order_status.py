# Generated by Django 4.0.3 on 2022-04-19 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('ordered', 'Заказано'), ('canceled', 'Отменено')], default='ordered', max_length=50, verbose_name='Статус заказа'),
        ),
    ]
