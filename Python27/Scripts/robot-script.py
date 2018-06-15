#!D:\apps\Python27\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'robotframework==3.1a1','console_scripts','robot'
__requires__ = 'robotframework==3.1a1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('robotframework==3.1a1', 'console_scripts', 'robot')()
    )
