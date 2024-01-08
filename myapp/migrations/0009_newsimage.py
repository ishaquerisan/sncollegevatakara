# Generated by Django 4.2.5 on 2024-01-08 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_news_image_delete_newsimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='news_images/')),
                ('news_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='myapp.news')),
            ],
        ),
    ]