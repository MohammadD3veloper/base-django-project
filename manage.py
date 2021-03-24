#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import colorama


def main():
    
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')
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
    print(colorama.Fore.RED+"""
██████╗ ██████╗    ██████╗ ██████╗ ██╗   ██╗██╗██╗      █████╗ ███╗   ███╗
██╔══██╗██╔══██╗   ██╔══██╗╚════██╗██║   ██║██║██║     ██╔══██╗████╗ ████║
██║  ██║██████╔╝   ██║  ██║ █████╔╝██║   ██║██║██║     ███████║██╔████╔██║
██║  ██║██╔══██╗   ██║  ██║ ╚═══██╗╚██╗ ██╔╝██║██║     ██╔══██║██║╚██╔╝██║
██████╔╝██║  ██║██╗██████╔╝██████╔╝ ╚████╔╝ ██║███████╗██║  ██║██║ ╚═╝ ██║
╚═════╝ ╚═╝  ╚═╝╚═╝╚═════╝ ╚═════╝   ╚═══╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
                    Django base project v 1.0 .......
                    The base of any django project ..
                    Api comming soon at new project !
                Follow me at : http://github.com/DrD3ViLaM
                In Telegram  : http://t.me/DrD3ViLaM 
""")
    main()
