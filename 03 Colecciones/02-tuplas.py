# tuplas - it is inmutables

tupla = (1, 5, "hello", [1,2,3], 1.2, True, 5)

print(tupla)
print(tupla[1])
print(tupla[-1])
print(tupla[1:])


# find
print("find:")
print(5 in tupla)
print(tupla.index(5))
print(tupla.count(5))
print(len(tupla))

# transform
print("transform")
list = list(tupla)
print(list)
tupla1 = tuple(list)
print(tupla1)