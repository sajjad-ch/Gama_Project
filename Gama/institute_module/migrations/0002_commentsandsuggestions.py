# Generated by Django 5.1.7 on 2025-04-12 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("institute_module", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CommentsAndSuggestions",
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
                (
                    "first_name_and_last_name",
                    models.CharField(max_length=128, verbose_name="نام و نام خانوادگی"),
                ),
                (
                    "phone_number",
                    models.CharField(max_length=11, verbose_name="تلفن همراه"),
                ),
                ("comment_or_suggestion", models.TextField()),
            ],
            options={
                "verbose_name": "نظر یا پیشنهاد",
                "verbose_name_plural": "نظرات و پیشنهادات",
            },
        ),
    ]
