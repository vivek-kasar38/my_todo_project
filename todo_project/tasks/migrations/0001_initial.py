# Generated by Django 5.0.7 on 2024-08-05 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('completed', models.BooleanField(default=False)),
                ('due_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
