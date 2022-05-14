#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import socket, subprocess
import logging

from django.shortcuts import redirect



ip = "127.0.0.1"
port = "8000"




def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Educacion_Estrella.settings')
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
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, int(port)))
        s.shutdown(2)
    except socket.error:
        logging.critical("EL SERVIDOR SE DETUVO INESPERADAMENTE")
        print("REINICIANDO EL SERVIDOR...")
        subprocess.call(['python', 'manage.py', 'runserver'])
