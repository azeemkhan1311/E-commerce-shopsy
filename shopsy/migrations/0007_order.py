# Generated by Django 4.2.5 on 2023-10-20 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("shopsy", "0006_alter_signup_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address", models.CharField(blank=True, max_length=100, null=True)),
                ("mobile", models.BigIntegerField(blank=True, null=True)),
                ("price", models.IntegerField()),
                ("quantity", models.IntegerField()),
                ("status", models.BooleanField(default=False)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="shopsy.signup"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="shopsy.product"
                    ),
                ),
            ],
        ),
    ]
