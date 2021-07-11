
fruitlist1 = [8,5,4,7,8,9,6,5,8,7,4,9,6,4,8,4,7,6,5,9]
fruitlist2 = [5,1,2,5,4,6,3,4,5,6,3,1,5,2,4,5,6,3]

print(list(set(fruitlist1) | set(fruitlist2)))
print(list(set(fruitlist1) - set(fruitlist2)))
print(list(set(fruitlist2) - set(fruitlist1)))
print(list(set(fruitlist2) & set(fruitlist1)))