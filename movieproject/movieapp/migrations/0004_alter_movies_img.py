# Generated by Django 4.2 on 2023-04-11 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0003_alter_movies_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='img',
            field=models.ImageField(upload_to='gallery'),
        ),
    ]