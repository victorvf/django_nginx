# Generated by Django 2.1.7 on 2019-03-10 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamento', '0002_auto_20190309_2027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour_value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('month_value', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Rotary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input', models.DateTimeField()),
                ('output', models.DateTimeField(blank=True, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estacionamento.Vehicle')),
            ],
        ),
    ]
