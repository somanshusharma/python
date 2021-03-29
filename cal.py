a = int(input("Enter value: "))
b = int(input("Enter value: "))
print("1. Addition")
print("2. Multiplication")
print("3. Substraction")
print("4. Division")
choice = int(input("Enter your choice"))
if(choice == 1):
    print(a+b)
elif(choice == 2):
    print(a*b)
elif(choice == 3):
    print(a-b)
elif(choice == 4):
    print(a/b)
else:
    print("Invalid")


