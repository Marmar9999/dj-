#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import django

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project2.settings')
    django.setup()      #..
    # Now you can import your Django models and run your script
    #from api.models import MyModel       #..

    try:
        from django.core.management import execute_from_command_line
        #execute_from_command_line(sys.argv)  #..
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    execute_from_command_line(sys.argv)
    

if __name__ == '__main__':
    main()
