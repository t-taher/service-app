# Generated by Django 3.2.10 on 2022-02-01 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0008_auto_20220131_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conatact',
            name='company',
            field=models.CharField(blank=True, max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='conatact',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
