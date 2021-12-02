# Generated by Django 3.2.9 on 2021-12-02 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20211202_2139'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectmember',
            options={'verbose_name': 'участник проекта', 'verbose_name_plural': 'участники проектов'},
        ),
        migrations.RemoveField(
            model_name='project',
            name='communication_links',
        ),
        migrations.RemoveField(
            model_name='project',
            name='design_links',
        ),
        migrations.RemoveField(
            model_name='project',
            name='documentation_links',
        ),
        migrations.RemoveField(
            model_name='project',
            name='organisation_links',
        ),
        migrations.AddField(
            model_name='project',
            name='more_info',
            field=models.TextField(blank=True, verbose_name='дополнительная информация'),
        ),
        migrations.CreateModel(
            name='ProjectLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='название')),
                ('link', models.URLField(verbose_name='ссылка')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='projects.project', verbose_name='проект')),
            ],
        ),
    ]
