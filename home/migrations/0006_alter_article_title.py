# Generated by Django 4.1.2 on 2022-11-13 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_news_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
