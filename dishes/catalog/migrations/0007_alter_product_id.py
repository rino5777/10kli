# Generated by Django 3.2.9 on 2021-12-13 16:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20211127_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]