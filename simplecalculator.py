print("~~~~~Mini Calculator~~~~~")
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
print("press 1 for addition \npress 2 for substraction \npress 3 for multiplication \npress 4 for division")
choice = int(input("select operation: "))
if choice == 1:
  print(num1+num2)
if choice == 2:
  print(num1-num2)
if choice == 3:
  print(num1*num2)
if choice == 4:
  print(num1/num2)