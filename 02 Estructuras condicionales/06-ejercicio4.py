# exercist four - calculator

firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))
operator = input("Enter the operation that want to perform. Example (s or S = sum, r or R = sustraction, p or P or m or M = multiplications, d or D = divitions: ").upper()
result = "";

if operator == "S":
    result = firstNumber + secondNumber;
elif operator == "R":
    result = firstNumber - secondNumber;
elif operator == "M" or operator == "P":
    result = firstNumber * secondNumber;
elif operator == "D":
    result = firstNumber / secondNumber;
else:
    print("operation incorrect")
if result != "":
    print(f"the result is {result:.2f}")