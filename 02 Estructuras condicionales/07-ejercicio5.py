# cajero automatico

wallet = 1000

operation = int(input("what is your wallet? \n1. Input cash in the wallet\n2. widraw\n3. show cash\n4. Exit\n"))

if operation == 1:
    wallet += float(input("Enter cash: "))
    print(f"your cash is {wallet}$")
elif operation == 2:
    cash = float(input("Enter cash: "))
    if cash <= wallet:
        print(f"your cash is {wallet}$")
    else:
        print("the windrat supera the cash in your wallet")
elif operation == 3:
    print(f"your cash is {wallet}$")
elif operation == 4:
    print("GoodBye")
else:
    print("Error operation invalit")