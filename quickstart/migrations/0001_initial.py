# Generated by Django 4.2.8 on 2025-02-03 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Klub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('negara', models.CharField(max_length=50)),
                ('stadion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('nim', models.CharField(max_length=100, unique=True)),
                ('prodi', models.CharField(max_length=100)),
                ('fakultas', models.CharField(max_length=100)),
                ('jenis_kelamin', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pemain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('umur', models.IntegerField()),
                ('posisi', models.CharField(max_length=50)),
                ('negara', models.CharField(max_length=50)),
            ],
        ),
    ]
