# Generated by Django 4.0 on 2022-04-25 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_id_emailid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='id',
            name='cellno',
            field=models.BigIntegerField(default=0),
        ),
    ]
