# Generated by Django 2.2.4 on 2020-06-25 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200625_1319'),
        ('appointments', '0003_auto_20200625_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.CharField(blank=True, max_length=500)),
                ('appointment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appointments.Appointment')),
                ('clint', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Clown')),
            ],
        ),
    ]
