# Generated by Django 4.1.6 on 2023-04-03 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ChambreCategory",
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
                ("name", models.CharField(default="--", max_length=30)),
                ("description", models.TextField(default="--", max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Chambre",
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
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("capacity", models.IntegerField(null=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=8)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="chambre.chambrecategory",
                    ),
                ),
            ],
        ),
    ]
