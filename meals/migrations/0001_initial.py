# Generated by Django 3.0.4 on 2020-03-18 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_id', models.IntegerField()),
                ('meal_id', models.IntegerField()),
                ('item', models.CharField(max_length=100)),
            ],
        ),
    ]
