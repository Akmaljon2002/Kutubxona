# Generated by Django 4.1.5 on 2023-01-07 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Muallif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('tugilgan_yili', models.DateField()),
                ('tirik', models.BooleanField()),
                ('kitob_soni', models.SmallIntegerField()),
                ('jins', models.CharField(choices=[('Erkak', 'Erkak'), ('Ayol', 'Ayol')], max_length=10)),
            ],
        ),
    ]
