# Generated by Django 4.1.4 on 2023-02-09 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_student_attempted_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='dashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cand_name', models.CharField(max_length=50)),
                ('progress_score', models.IntegerField()),
            ],
        ),
    ]