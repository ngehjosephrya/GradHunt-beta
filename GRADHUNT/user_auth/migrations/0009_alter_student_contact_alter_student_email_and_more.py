# Generated by Django 4.1.5 on 2023-08-24 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0008_alter_student_contact_alter_student_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='contact',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='speciality',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
