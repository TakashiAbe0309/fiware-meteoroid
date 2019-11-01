# Generated by Django 2.2.6 on 2019-11-01 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endpoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fiware_service', models.CharField(blank=True, default='', max_length=64)),
                ('fiware_service_path', models.CharField(default='/', max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('path', models.CharField(max_length=64)),
                ('method', models.CharField(max_length=8)),
                ('funciton', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Function')),
            ],
            options={
                'unique_together': {('name', 'path', 'method', 'fiware_service', 'fiware_service_path')},
            },
        ),
        migrations.DeleteModel(
            name='Result',
        ),
    ]
