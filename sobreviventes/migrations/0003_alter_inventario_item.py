# Generated by Django 4.0.1 on 2022-01-10 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sobreviventes', '0002_inventario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='item',
            field=models.CharField(choices=[('Água', 'Água'), ('Alimentação', 'Alimentação'), ('Medicação', 'Medicação'), ('Munição', 'Munição')], max_length=15),
        ),
    ]
