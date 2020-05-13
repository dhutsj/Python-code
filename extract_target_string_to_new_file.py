import re

with open("to_replace.txt", "rb") as f:
    for line in f.readlines():
        match = re.match(r'(.*) \'(.*)\'', line)
        print match.group(2)

with open("to_replace.txt", "rb") as f:
    with open("vvvv.txt", 'wb') as r:
        for line in f.readlines():
            match = re.match(r'(.*) \'(.*)\'', line)
            r.write(match.group(2))
            r.write("\n")
