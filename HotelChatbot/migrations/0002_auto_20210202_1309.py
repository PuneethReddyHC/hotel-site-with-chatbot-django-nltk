# Generated by Django 2.2.17 on 2021-02-02 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelChatbot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='image',
            field=models.CharField(max_length=245),
        ),
    ]
