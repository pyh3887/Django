# Generated by Django 3.0.6 on 2020-05-22 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sangpum2',
            fields=[
                ('sang_id', models.AutoField(primary_key=True, serialize=False)),
                ('sang_val', models.IntegerField(max_length=10)),
                ('sang_name', models.CharField(max_length=10)),
                ('sang_pay', models.CharField(max_length=10)),
                ('sang_stock', models.CharField(max_length=10)),
                ('sang_explain', models.CharField(max_length=100)),
            ],
        ),
    ]
