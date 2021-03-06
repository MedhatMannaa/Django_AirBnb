# Generated by Django 3.1.1 on 2020-09-24 11:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Area')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='City')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Country')),
            ],
        ),
        migrations.CreateModel(
            name='Furniture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Furniture')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Room')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, unique=True, verbose_name='Unit Title')),
                ('description', models.TextField(max_length=500, verbose_name='Unit Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('num_bedrooms', models.IntegerField(verbose_name='Number of Bed rooms')),
                ('hole_space', models.IntegerField(verbose_name='Hole Space')),
                ('active', models.BooleanField(default=True)),
                ('owner_email', models.EmailField(default='m.medhat@dropsgroup.com', max_length=254)),
                ('type', models.CharField(choices=[('CHALEH', 'CHALEH'), ('ROOM', 'ROOM'), ('FLAT', 'FLAT'), ('STUDIO', 'STUDIO'), ('Lounge', 'Lounge')], default='FLAT', max_length=20)),
                ('status', models.CharField(choices=[('AVAILABLE TO RENT', 'AVAILABLE TO RENT'), ('RENTED', 'RENTED'), ('AVAILABLE TO SELL', 'AVAILABLE TO SELL'), ('SOLD', 'SOLD'), ('SUSPENDED', 'SUSPENDED')], default='SUSPENDED', max_length=20)),
                ('remarks', models.TextField(blank=True, max_length=500, null=True, verbose_name='Remarks')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('Room', models.ManyToManyField(to='units.Room')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='units.area')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='units.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='units.country')),
                ('furniture', models.ManyToManyField(to='units.Furniture')),
            ],
        ),
    ]
