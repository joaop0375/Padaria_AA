# Generated by Django 4.2.7 on 2023-11-27 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_padaria_aa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='encomenda',
            name='data_entrega',
        ),
        migrations.AddField(
            model_name='encomenda',
            name='quantidade',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='encomenda',
            name='produto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_padaria_aa.produto'),
        ),
    ]
