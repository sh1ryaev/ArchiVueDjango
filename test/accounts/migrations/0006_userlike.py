# Generated by Django 3.2.13 on 2022-06-16 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_postphotos_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.BigIntegerField(verbose_name='Номер пользователя')),
                ('id_post', models.BigIntegerField(verbose_name='Номер поста')),
            ],
        ),
    ]
