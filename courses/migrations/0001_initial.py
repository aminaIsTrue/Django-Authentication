# Generated by Django 3.2 on 2021-05-04 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='course-pics')),
                ('duration', models.PositiveIntegerField()),
                ('is_new', models.BooleanField(default=False)),
                ('price', models.PositiveIntegerField()),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Updating_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
