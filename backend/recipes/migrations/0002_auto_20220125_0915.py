# Generated by Django 2.2.26 on 2022-01-25 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to='recipes/images', verbose_name='Картинка'),
        ),
    ]
