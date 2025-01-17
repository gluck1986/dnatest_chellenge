# Generated by Django 5.1.4 on 2024-12-15 19:06

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_name', models.CharField(max_length=255)),
                ('species', models.CharField(max_length=255)),
                ('test_date', models.DateField()),
                ('milk_yield', models.FloatField()),
                ('health_status', models.CharField(max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
