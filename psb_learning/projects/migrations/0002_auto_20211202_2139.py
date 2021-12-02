# Generated by Django 3.2.9 on 2021-12-02 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='communication_links',
            field=models.TextField(blank=True, verbose_name='ссылки на ресурсы коммуникации'),
        ),
        migrations.AddField(
            model_name='project',
            name='design_links',
            field=models.TextField(blank=True, verbose_name='ссылки на ресурсы дизайна'),
        ),
        migrations.AddField(
            model_name='project',
            name='documentation_links',
            field=models.TextField(blank=True, verbose_name='ссылки на ресурсы документации'),
        ),
        migrations.AddField(
            model_name='project',
            name='events',
            field=models.TextField(blank=True, verbose_name='обязательные мероприятия'),
        ),
        migrations.AddField(
            model_name='project',
            name='goals',
            field=models.TextField(blank=True, verbose_name='цели и задачи'),
        ),
        migrations.AddField(
            model_name='project',
            name='organisation_links',
            field=models.TextField(blank=True, verbose_name='ссылки на ресурсы организации'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_type',
            field=models.CharField(blank=True, max_length=512, verbose_name='тип проекта'),
        ),
        migrations.AddField(
            model_name='project',
            name='results',
            field=models.TextField(blank=True, verbose_name='результаты проекта'),
        ),
        migrations.AddField(
            model_name='project',
            name='stages',
            field=models.TextField(blank=True, verbose_name='план работы и контрольные точки'),
        ),
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.TextField(blank=True, verbose_name='стек технологий'),
        ),
        migrations.CreateModel(
            name='ProjectMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='ФИО')),
                ('role', models.CharField(max_length=512, verbose_name='должность')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='фотография')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='projects.project', verbose_name='проект')),
            ],
            options={
                'verbose_name': 'файл проекта',
                'verbose_name_plural': 'файлы проектов',
            },
        ),
        migrations.CreateModel(
            name='ProjectFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='', verbose_name='файл')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='projects.project', verbose_name='проект')),
            ],
            options={
                'verbose_name': 'файл проекта',
                'verbose_name_plural': 'файлы проектов',
            },
        ),
    ]