name = input("enter your name:")
family = input("enter your family:")
a = int(input("enter score 1:"))
b = int(input("enter score 2:"))
c = int(input("enter score 3:"))
average = (a+b+c)/3

if average >=17:
    print(name,family,"great")
if 17 > average >= 12:
    print(name,family,"normal")
if average < 12:
    print(name,family,"fail")
