# Generated by Django 5.1.1 on 2024-09-25 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_review_review_user_alter_review_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='total_review',
            field=models.IntegerField(default=0),
        ),
    ]