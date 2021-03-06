# Generated by Django 3.2.10 on 2022-01-03 22:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_alter_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
