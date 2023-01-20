#!/usr/bin/python3
import re
n = """@moussa10.\n
[Verse 3]@moussa11[Verse 4]@moussa12
[Verse 5]@moussa1013
"""

i = re.findall('@[a-z\d]+', n, re.MULTILINE)

print('\n'.join(i))
