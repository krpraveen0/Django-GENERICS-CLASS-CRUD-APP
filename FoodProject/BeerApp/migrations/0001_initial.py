# Generated by Django 4.0.1 on 2022-01-24 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('taste', models.CharField(max_length=150)),
                ('color', models.CharField(max_length=150)),
                ('price', models.FloatField()),
            ],
        ),
    ]
