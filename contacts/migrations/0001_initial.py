# Generated by Django 3.2.5 on 2021-07-23 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('contact_id', models.IntegerField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=25)),
                ('mname', models.CharField(max_length=25)),
                ('lname', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='phone',
            fields=[
                ('phone_id', models.IntegerField(primary_key=True, serialize=False)),
                ('phone_type', models.CharField(max_length=15)),
                ('area_code', models.CharField(max_length=3)),
                ('number', models.CharField(max_length=12)),
                ('contact_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.contact')),
            ],
        ),
        migrations.CreateModel(
            name='date',
            fields=[
                ('d_id', models.IntegerField(primary_key=True, serialize=False)),
                ('date_type', models.CharField(max_length=20)),
                ('d_date', models.DateField()),
                ('contact_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.contact')),
            ],
        ),
        migrations.CreateModel(
            name='address',
            fields=[
                ('address_id', models.IntegerField(primary_key=True, serialize=False)),
                ('address_type', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=35)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=15)),
                ('zip', models.CharField(max_length=5)),
                ('contact_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.contact')),
            ],
        ),
    ]
