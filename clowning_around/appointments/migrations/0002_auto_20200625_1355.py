# Generated by Django 2.2.4 on 2020-06-25 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Appointment_Status',
        ),
        migrations.AlterField(
            model_name='requestclientdetailss',
            name='clown',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
