import inflect
# inflect.engine().join(list) convert a LIST into a STR with "," and one last "and"
# print Adieu, adieu plus the names separated by  ',' and the last with 'and'
# n - 1 => ','  one 'and'

names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except(EOFError):
        print()
        break
names = inflect.engine().join(names)
print(f"Adieu, adieu, to {names}")
