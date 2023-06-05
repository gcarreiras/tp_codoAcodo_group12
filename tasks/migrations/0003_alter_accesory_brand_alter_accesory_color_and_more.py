# Generated by Django 4.2 on 2023-05-21 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_accesory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesory',
            name='brand',
            field=models.CharField(max_length=50, verbose_name='Accesory brand'),
        ),
        migrations.AlterField(
            model_name='accesory',
            name='color',
            field=models.CharField(max_length=50, verbose_name='Accesory color'),
        ),
        migrations.AlterField(
            model_name='accesory',
            name='description',
            field=models.CharField(max_length=100, verbose_name='Accesory description'),
        ),
        migrations.AlterField(
            model_name='accesory',
            name='image',
            field=models.FileField(upload_to='', verbose_name='Accesory image'),
        ),
        migrations.AlterField(
            model_name='accesory',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Accesory name'),
        ),
        migrations.AlterField(
            model_name='accesory',
            name='price',
            field=models.FloatField(verbose_name='Accesory price'),
        ),
    ]