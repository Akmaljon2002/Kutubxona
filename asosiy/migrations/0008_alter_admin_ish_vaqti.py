# Generated by Django 4.1.5 on 2023-01-29 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0007_remove_record_qatargan_sana_record_qaytargan_sana'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='ish_vaqti',
            field=models.CharField(choices=[('8:00 - 14:00', '8:00 - 14:00'), ('14:00 - 16:00', '14:00 - 16:00'), ('16:00 - 19:00', '16:00 - 19:00')], max_length=30),
        ),
    ]