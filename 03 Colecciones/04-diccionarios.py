# diccionary

dic = {}

print(dic)

dic = {"azul":"blue", "rojo":"red", "verde":"green"}

print(dic)

# print value the a element
print("print value the a element")
print(dic["azul"])

# add element
print("add element")
dic["amarillo"] = "yelow"
print(dic)

# edit element
print("edit element")
dic["azul"]="BLUE"
print(dic)

# delete element
print("delete elemet")
del(dic["verde"])
print(dic)

# type the value
print("type the value")
dic = {"jampool":[26,1.70], "yorgelis":[22,1.65], "stifen":[4,1.10]}
print(dic)
dic = {"jampool":{"age":26,"alt":1.70}, "yorgelis":[22,1.65], "stifen":[4,1.10]}
print(dic)
print(dic["jampool"])

# dicionary 2
print("dicionary 2")
team = {10:"paulo dybala", 11:"douglas costa", 7:"cristiano ronaldo", 17:"mario"}
print(team)
print(team[10])
print(team.get(7, "no exit"))
print(team.get(6, "no exit"))

# find
print("find:")
print(10 in team)
print(6 in team)
print(team.keys())
print(team.values())
print(team.items())

# lenght
print("lenght")
print(len(team))

# clear
print("clear")
team.clear()
print(team)


