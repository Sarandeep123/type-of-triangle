a=int(input("Enter the side a:"))
b=int(input("Enter the side b:"))
c=int(input("Enter the side c:"))
if a==b and b==c:
    print("It is an equilaterial triangle")
elif a!=b and b!=c:
    print("It is a scalene triangle")
else:
    print("It is an isosceles triangle")
