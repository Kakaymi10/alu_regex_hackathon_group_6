#!/usr/bin/python3
import re

n = """Show #ABD457
#ABD455 Name #ABD456 Episode #ABD459"""

i = re.findall('#[a-zA-Z0-9]{6}', n, re.MULTILINE)

print('\n'.join(i))
