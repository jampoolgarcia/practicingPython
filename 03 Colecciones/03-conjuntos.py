# conjuntos - values desordent and unique

conj = set()
conj = {1, 2, 3, "hello", 4.54, 1, 2, 3}

print(conj)

# add element
print("add element")
conj.add(5)
conj.add("bye")
print(conj)

# delete
print("delete element")
conj.discard(3)
print(conj)

# find
print("find element")
print(2 in conj)
print(3 in conj)
print(2 not in conj)

# clear
print("clear element")
conj.clear()
print(conj)

# conjuntos 2
print("conjunt part 2")
a = {1,2,3}
b = {3,4,5}
print(a==b)
c = {3,2,1}
print(a==c)

# union
print("union")
d = a | b
print(d)

# intersection
print("intersection")
e = a & b
print(e)

# diferent
print("diferent")
f = a - b
print(f)
g = b - a
print(g)

# diferent asimetrict
print("diferent asimetrict")
h = a ^ b
print(h)

# dertemitation sub-conjunt
print("dertemitation sub-conjunt")
i = {1,2,3,4,5,6}
print(a.issubset(i))
print(i.issuperset(b))
print(a.isdisjoint(b))

# conjunt inmutable
a = frozenset({7,8,9})
