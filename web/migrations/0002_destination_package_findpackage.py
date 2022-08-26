# Generated by Django 4.1 on 2022-08-26 04:51

from django.db import migrations, models
import django.db.models.deletion
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_place', models.CharField(max_length=225)),
                ('to_place', models.CharField(max_length=225)),
            ],
            options={
                'verbose_name_plural': 'Destination',
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='package/', verbose_name='Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
                ('days', models.CharField(max_length=225)),
                ('amount', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Packages',
            },
        ),
        migrations.CreateModel(
            name='FindPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persons', models.IntegerField()),
                ('date', models.DateField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.destination')),
            ],
            options={
                'verbose_name_plural': 'FindPackage',
            },
        ),
    ]