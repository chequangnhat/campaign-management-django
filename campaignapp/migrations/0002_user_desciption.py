# Generated by Django 4.1.5 on 2023-02-06 02:29

from django.db import migrations, models


def add_user_description(apps, scheme_editor):

    User = apps.get_model('campaignapp', 'User')
    users = User.objects.all()

    for user in users:
        user.description = f"{user.first_name} {user.last_name}'s description"
        user.save()


def reverse_user_description(apps, scheme_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('campaignapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.TextField(default="desc"),
            preserve_default=False,
        ),
        migrations.RunPython(add_user_description,
                             reverse_code=reverse_user_description),
    ]
