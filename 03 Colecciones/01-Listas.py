# Lists

# print list
print("list")
list = ["monday", "tuesday", "tursday", "wenesday", "friday", "saturday", "sunday"]
print(list)

# print one element list
print("element list")
print(list[0])

# print element list with index negative
print("index negative")
print(list[-1])

# print element list with slasin
print("slasin")
print(list[0:-6])
print(list[:-5])
print(list[:-4])
print(list[:-3])
print(list[:-2])
print(list[:-1])
print(list[:])
print(list[:7])
print(list[:6])
print(list[:5])
print(list[:4])
print(list[:3])
print(list[:2])
print(list[:1])

# print type element in a list
print("type of element the list")
list = ["monday", 40, 30.8, True, ["saturday", "sunday"]]
print(list)

# get count element list
print("count list")
print(len(list))

# add element last list = list.append(addElement)
print("add element lasty list")
list.append("last")
print(list)

# add element in a position = list.insert(index, addElement)
print("add element in a position")
list = [ 1, 2, 4, 5]
list.insert(2,3)
print(list)

# add many element in the list = list.extend(addElement, addElement, addElement)
print("add many element")
list.extend([6,7,8])
print(list)

# sun list
print("sun list")
list1 = [ 1, 2, 3, 4]
list2 = [ 5, 6, 7, 8]
list3 = list1 + list2
print(list3)

# find element in the list
print("find element in the list")
print(3 in list)
list.append("jampool")
print("jampool" in list)
print(10 in list)

# find element and get index in the list
print("find element and get index in the list")
print(list.index(3))
print(list.index("jampool"))

# find and count element repeat in the list
print("find and count element repeat in the list")
list = [1, 2, 4, 5, "jampool", 1 , 3, 5, "jampool", 1]
print(list.count(1))
print(list.count("jampool"))
print(list.count(10))

# delete elemnets of the list for index
print("delete elemnets of the list for index")
print(list)
list.pop()
print(list)
list.pop(-1)
print(list)
list.pop(5)
print(list)

# delete elemnets of the list for value
print("delete elemnets of the list  for value")
print(list)
list.remove(3)
print(list)
list.remove("jampool")
print(list)

# clear list
print("clear list")
print(list)
list.clear()
print(list)

# reverse list
print("reverse list")
list = [ 1, 2, 3, 4]
print(list)
list.reverse()
print(list)

# mutiplications elements
print("multiplication elements")
list = [ 1, 2, 3, 4]*2
print(list)

# order elements (int)
print("order elements")
list = [ -1, 0, 7, 10, -8, 2, 3, 4]
list.sort()
print(list)
list.sort(reverse = True)
print(list)
