# Generated by Django 2.2.3 on 2019-07-04 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('details', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('IN', 'Nota Fiscal'), ('OT', 'Outro')], default=('IN', 'Nota Fiscal'), max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('details', models.CharField(blank=True, max_length=255)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order.Invoice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OrderTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='order.Order')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stock.Transaction')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order.InvoiceCategory'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='payer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='order.Payer'),
        ),
    ]
