# Generated by Django 5.0.7 on 2024-07-23 17:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contents", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sitecontent",
            name="value",
            field=models.TextField(),
        ),
    ]
