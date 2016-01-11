#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ithacash.settings.local")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ithacash_dev.settings.local")
>>>>>>> refs/remotes/origin/master

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
