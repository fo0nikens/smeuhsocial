#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":
    apps_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "apps")
    sys.path.insert(0, apps_dir)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
