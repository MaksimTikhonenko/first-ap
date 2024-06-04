# Generated by Django 5.0.6 on 2024-06-04 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('expire_date', models.DateTimeField(null=True)),
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]