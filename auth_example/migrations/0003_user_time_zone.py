"""
    auth_example/migrations/0003_user_time_zone.py is part of Demo MisionTIC-2021 C4, 
    created by Carlos Andrés Sierra.

    Demo MisionTIC-2021 C4 is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Demo MisionTIC-2021 C4 is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Demo MisionTIC-2021 C4. If not, see <https://www.gnu.org/licenses/>.

    For contact, you can write to casierrav@unal.edu.co
"""


# Generated by Django 3.2.9 on 2021-12-09 04:33

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('auth_example', '0002_delete_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='time_zone',
            field=models.CharField(default='America/Bogota', max_length=50, verbose_name='TimeZone'),
        ),
    ]