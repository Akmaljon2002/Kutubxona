# Generated by Django 4.1.5 on 2023-01-24 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0005_alter_talaba_bitiruvchi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muallif',
            name='tirik',
            field=models.BooleanField(default=True),
        ),
    ]