# Generated by Django 3.0.5 on 2020-07-15 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Attendence_a', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.CharField(max_length=50)),
                ('class_c', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Add_class',
            },
        ),
        migrations.CreateModel(
            name='Add_student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=10)),
                ('first_n', models.CharField(max_length=20, null=True)),
                ('last_n', models.CharField(max_length=20, null=True)),
                ('email_id', models.EmailField(max_length=254, null=True)),
                ('teacher_id', models.CharField(max_length=50, null=True)),
                ('subject', models.CharField(max_length=50, null=True)),
                ('class_c', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'Add_student',
            },
        ),
        migrations.CreateModel(
            name='Add_subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Add_subject',
            },
        ),
    ]