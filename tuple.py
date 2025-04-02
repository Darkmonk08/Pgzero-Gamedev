#creating tuple/packing
address=(4,"Shanti Niketan","New Delhi","India")
print(address)
print(type(address))

#retrive items
City=address[2]
print(City)

#retrive all items
for i in address:
    print(i)
    
#unpacking
hnum,street,city,country=address
print(hnum)
print(street)
print(city)
print(country)

#one item tuple
studentsnum=(4,)

#check type
print(type(studentsnum))

#print lenght
print(len(studentsnum))

#slicing the tuple/getting a section of the tuple(same as list, ending index is not included)
print(address[0:2])
#first item till ending index
print(address[:3])
#first index till end
print(address[1:])
#reverse tuple
print(address[ : :-1])