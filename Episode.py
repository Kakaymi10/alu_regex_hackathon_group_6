import re
n = """show Name S23E34: Episode Title
show Name S23E34: Episode Title"""

i=re.findall('[A-Za_z ]+\sS\d{2}E\d{2}:[A-Za-z ]+' n, re.MULTILINE)

print('\n'.join(i))
