# Generated by Django 4.2.6 on 2023-10-26 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='pic',
            field=models.ImageField(default='no_picture.jpg', upload_to='recipes'),
        ),
    ]
