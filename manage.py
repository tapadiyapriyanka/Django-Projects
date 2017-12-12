#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "simple_project.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "helloworld_project.settings")
>>>>>>> 171f531816a2bab6ba61924e93f9b7a677a82750
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
