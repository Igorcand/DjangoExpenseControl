# Generated by Django 4.1.1 on 2022-10-04 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0003_alter_transacao_options_alter_transacao_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(),
        ),
    ]
