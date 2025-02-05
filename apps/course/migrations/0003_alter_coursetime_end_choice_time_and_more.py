# Generated by Django 4.1.7 on 2023-09-10 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0002_alter_coursetype_logo_alter_coursetype_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coursetime",
            name="end_choice_time",
            field=models.DateTimeField(verbose_name="选课结束时间"),
        ),
        migrations.AlterField(
            model_name="coursetime",
            name="start_choice_time",
            field=models.DateTimeField(verbose_name="选课开始时间"),
        ),
    ]
