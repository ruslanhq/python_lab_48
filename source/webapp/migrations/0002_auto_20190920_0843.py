# Generated by Django 2.2 on 2019-09-20 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Other', 'Other'), ('phone', 'Phone'), ('pc', 'Personal computer'), ('camera', 'Camera')], default='Other', max_length=20, verbose_name='Category'),
        ),
    ]