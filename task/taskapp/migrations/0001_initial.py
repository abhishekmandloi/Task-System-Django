# Generated by Django 3.2.7 on 2021-09-10 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('name', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=400)),
                ('link_id', models.AutoField(primary_key=True, serialize=False)),
                ('datecreated', models.DateTimeField()),
                ('datelastmodified', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskapp.task')),
            ],
        ),
    ]
