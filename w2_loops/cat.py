print("\nwhile\n")

i = 0
while i  < 3:
    print("meow")
    i += 1

print("\nfor\n")

for i in range(3):
    print("miau")

# if I don't care about the variable to iterate can use _
for _ in range(3):
    print("miau")

print("meau\n" * 3, end="")

while True:
    n  = int(input("What's n?"))
    if n > 0:
        break

for _ in range(n):
    print("miuau")
