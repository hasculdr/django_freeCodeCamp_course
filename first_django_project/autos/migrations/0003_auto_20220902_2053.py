# Generated by Django 3.2.14 on 2022-09-02 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0002_alter_manufacturer_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auto',
            old_name='auto',
            new_name='make',
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Maker'),
        ),
    ]
