import sys

# sys.argv gives you a list from the prompt

"""
try:
    print("hello my name is", sys.argv[1])
except (IndexError):
    print("two few arguments")
    pass
"""

# Check for errors
if len(sys.argv) < 2:
    sys.exit("to few arguments")

for arg in sys.argv[1:]:
    print("hello my name is", arg)

# Print name Tag
#print("hello my name is", sys.argv[1])


print()

print(sys.argv)
