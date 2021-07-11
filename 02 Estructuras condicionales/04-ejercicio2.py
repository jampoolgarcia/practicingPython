# exercist two - make a program  that asks three numbers and i determined which is greater

firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))
thirdNumber = int(input("Enter third number: "))

''' 
    if secondNumber<firstNumber>thirdNumber:
        print(f"the fisrt number is greater")
    elif firstNumber<secondNumber>thirdNumber:
        print(f"the second number is greater")
    elif firstNumber<thirdNumber>secondNumber:
        print(f"the third number is greater")
    elif firstNumber==secondNumber>thirdNumber:
        print(f"the fisrt and second number is greater")
    elif firstNumber==thirdNumber>secondNumber:
        print(f"the fisrt and third number is greater")
    elif secondNumber==thirdNumber>firstNumber:
        print(f"the second and third number is greater")
    else:
        print(f"the numbers are the same")
'''

if secondNumber <= firstNumber >= thirdNumber:
    print(f"the number greater is {firstNumber}")
elif firstNumber <= secondNumber >= thirdNumber:
    print(f"the number greater is {secondNumber}")
elif firstNumber <= thirdNumber >= secondNumber:
    print(f"the number greater is {thirdNumber}")
