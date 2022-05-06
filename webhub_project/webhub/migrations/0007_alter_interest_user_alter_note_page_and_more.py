# Generated by Django 4.0.4 on 2022-05-06 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webhub', '0006_alter_interest_user_alter_note_page_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='interest', to='webhub.user'),
        ),
        migrations.AlterField(
            model_name='note',
            name='page',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='note', to='webhub.page'),
        ),
        migrations.AlterField(
            model_name='page',
            name='interest',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='page', to='webhub.interest'),
        ),
        migrations.AlterField(
            model_name='search',
            name='interest',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='search', to='webhub.interest'),
        ),
    ]