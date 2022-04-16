#Tuples are created with brackets and comma to separate values


tuple1 = ("Cristian", 30, "Rio de Janeiro")
print(tuple1)

#It can convert an iterable (list, dict, string) into a tuple using the built-in function
tuple2 = tuple(["Cristian", 30, "Rio de Janeiro"])
print(tuple2)

#Indexing the elements in a tuple
item = tuple2[0]
print(item)


#Iterating over a tuple by using for in loop
for i in tuple1:
    print(i)

#Using conditions to check for an element in a tuple
if "Rio de Janeiro" in tuple1:
    print("yes")
else:
    print("no")

#Converting a tuple into a list and vice versa
mylist = list(tuple1)
print(mylist)

tuple3 = tuple(mylist)
print(tuple3)

#Packing multiples elements at the same time and unpacking mltiples tuples

#Packing three elements to the tuple, it's necessary to match with the number of elements in a tuple
tuple4 = ("Ana", 15, "São Paulo") #3 elements
name, age, city = tuple4 #3 variables
print(name, age, city)

#unpacking multiples with *
my_tuple = (1, 2, 3, 4, 5, 6)

first_item, *items_btwn, last_item = my_tuple
print(first_item)
print(items_btwn)
print(last_item)

#Useful methods 

print(len(my_tuple)) #show how many elements inside the tuple
print(my_tuple.count(5)) #show how many '5' inside the tuple
print(my_tuple.index(3)) #show the index of an element in a tuple

concat_tuple = tuple1 + tuple4 #Concatenation
print(concat_tuple)

str_to_tuple = tuple("Cristian") #Convert a string to tuple
print(str_to_tuple)