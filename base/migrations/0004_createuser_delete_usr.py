# Generated by Django 4.0.1 on 2022-06-02 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_usr'),
    ]

    operations = [
        migrations.CreateModel(
            name='createuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='usr',
        ),
    ]
