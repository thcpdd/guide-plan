# Generated by Django 4.1.7 on 2023-10-16 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homework", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homework",
            name="size",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=13, verbose_name="文件大小"
            ),
        ),
    ]
