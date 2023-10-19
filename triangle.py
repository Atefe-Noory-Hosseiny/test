a = int(input("enter a:"))
b = int(input("enter b:"))
c = int(input("enter c:"))

if a < b + c and b < a + c and c < a + b:
    print("can be a triangle")
else:
    print("can not be a triangle")