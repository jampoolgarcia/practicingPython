# exercist one - make a program that asks for two numbers and shows which of them is par o if both are...

firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))

if firstNumber%2 == 0 and secondNumber == 0:
    print("Numbers are pairs")
elif firstNumber%2 == 0:
    print(f"the first number is couple")
elif secondNumber%2 == 0:
    print(f"the second number is par")
else:
    print("No number is torque")
