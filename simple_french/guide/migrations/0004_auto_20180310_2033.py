# Generated by Django 2.0.2 on 2018-03-10 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0003_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=255), unique=True),
        ),
    ]
