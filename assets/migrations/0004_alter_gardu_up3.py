# Generated by Django 4.2.8 on 2023-12-28 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_up3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gardu',
            name='up3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='assets.up3'),
        ),
    ]
