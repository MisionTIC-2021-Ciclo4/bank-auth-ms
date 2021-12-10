"""
    manage_dev.py is part of Demo MisionTIC-2021 C4, created by Carlos Andrés Sierra.

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


"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks in Development (localhost) environment."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bank_auth_example.settings_dev')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
