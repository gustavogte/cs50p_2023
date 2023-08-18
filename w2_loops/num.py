num = "aa010123"
num2 = ""
for i in num:
    print(i)
    if i.isdigit():
        num2 = num2 + i
print (num2)
if num2[0] == "0":
    print(False)
