# Generated by Django 4.2.10 on 2024-03-09 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_alter_clientes_created_at_alter_clientes_email_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Estoque',
        ),
    ]