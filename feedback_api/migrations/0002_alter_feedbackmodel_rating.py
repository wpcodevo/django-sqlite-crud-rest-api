# Generated by Django 5.1.3 on 2024-11-08 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackmodel',
            name='rating',
            field=models.FloatField(),
        ),
    ]
