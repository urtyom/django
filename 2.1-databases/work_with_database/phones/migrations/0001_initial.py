# Generated by Django 4.2.7 on 2023-11-21 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=20)),
                ('release_date', models.CharField(max_length=50)),
                ('lte_exists', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
    ]