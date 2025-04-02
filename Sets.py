marks=[87,93,94,93,67,78,87]
print(marks)
print(type(marks))
#convert to set
x=set(marks)
#verify type
print(type(x))
print(x)
#trying to retrive value using indexing(doesnt work)
# a=x[3]
# print(a)
#directly create set
fruits={"watermelon","mango","apple","orange"}
#adding item
fruits.add("Lemon")
print(fruits)
citrusfruits={"orange","lime","grapefruit"}
#set operations
#combining two sets
print(fruits.union(citrusfruits))
print(fruits|citrusfruits)
#intersection/common item(s)
print(fruits.intersection(citrusfruits))
print(fruits&citrusfruits)
#differance of sets
print(fruits.difference(citrusfruits))
print(fruits-citrusfruits)
#symetric differance
print(fruits.symmetric_difference(citrusfruits))
print(fruits^citrusfruits)