# Generated by Django 2.1.5 on 2019-01-18 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.CharField(max_length=255)),
                ('request_id', models.CharField(max_length=255)),
                ('order_id', models.IntegerField()),
                ('order_type', models.CharField(blank=True, max_length=255, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('state', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('processing', 'processing'), ('success', 'success'), ('failed', 'failed')], default='processing', max_length=255)),
                ('paid', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('error', models.TextField(blank=True, default='None', max_length=255, null=True)),
            ],
        ),
    ]
