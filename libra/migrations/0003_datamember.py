# Generated by Django 5.0.1 on 2024-02-15 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libra', '0002_records'),
    ]

    operations = [
        migrations.CreateModel(
            name='datamember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('mobile', models.IntegerField()),
                ('semester', models.IntegerField()),
                ('branch', models.CharField(max_length=40)),
            ],
        ),
    ]