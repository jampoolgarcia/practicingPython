# exercist three -


print("exercis three")
# my version
'''
    a = input("Enter the value of 'a': ")
    b = input("Enter the value of 'b': ")
    print(f"the value of 'a' is {a}, the value of 'b' is {b}")
    aux = a
    a = b
    b = aux
    print(f"the value of 'a' is {a}, the value of 'b' is {b}")
'''

# version correct in python
a = input("Enter the value of 'a': ")
b = input("Enter the value of 'b': ")
print(f"the value of 'a' is {a}, the value of 'b' is {b}")
a, b = b, a;
print(f"the value of 'a' is {a}, the value of 'b' is {b}")
