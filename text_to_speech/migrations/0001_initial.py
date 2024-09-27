# Generated by Django 4.2.7 on 2024-07-10 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Text_to_speech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(help_text='Введите текст, который вы хотите преобразовать в речь.', max_length=700, verbose_name='Текст')),
                ('file_name', models.CharField(help_text='Укажите имя аудиофайла.', max_length=200, unique=True, verbose_name='Имя файла')),
                ('voice', models.CharField(blank=True, help_text='Выберите голос для преобразования текста в речь.', max_length=400, null=True, verbose_name='Голос')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Дата и время создания записи.', verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Дата и время последнего обновления записи.', verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Текст в речь',
                'verbose_name_plural': 'Тексты в речь',
            },
        ),
    ]
