#Example of a list



city_list = ["Rio", "Nova Iguaçu", "Niterói"]
print(city_list)

#How to index the list items, it's checking the last item from the list.
item = city_list[2]
print(item)

#Iteraction using for, will print all items in a list
for i in city_list:
    print(i)

#Applying conditions in a list to check it.
if "Rio" in city_list:
    print("yes")
else:
    print("No")

#How to check the amount of the elements inside the list
print(len(city_list))

#Appending elements to a list
city_list.append("Macaé")

print(city_list)

#Inserting an especific element in a list (this exemple inserting Caxias to first position)
city_list.insert(0, "Caxias")
print(city_list)

#Removing the last item from a list and showing the element
item2 = city_list.pop()
print(item2)
print(city_list)

#Removing an especific element from a list
item3 = city_list.remove("Rio")
print(city_list)

#Clear all the list
# item4 = city_list.clear()
# print(city_list)

#Reverse the list
item5 = city_list.reverse()
print(city_list)

# Sorting the list
item5 = city_list.sort()
print(city_list)

# Slicing the list
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = num_list[1:5]
print (a)

#Convert string to a list

string_to_list = list("Cristian")
print(string_to_list)

#Methods to copy a list

l1 = [1]*5

l2 = l1[:] #First way
l3 = list(l1) #Second way
l4 = l1.copy() # Third way
print(l2, l3, l4)