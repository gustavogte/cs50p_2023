import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
#if matches:
    #last = matches.group(1)
    #first = matches.group(2)
    #name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
