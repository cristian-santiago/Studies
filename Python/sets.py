#Sets are unordered collectoon data type unidexded. mutable and has no duplicate elements.

#Empty set

emp_set = set()


my_set = {"car", "house", "people"}
print(my_set)

# Using set function and create from an iterable data.
my_set2 = set([1, 2, 3, 4, 5])
my_set2 = set((1, 2, 3, 4, 5))
print(my_set2)

#Sets don't allow duplicates and they are unordered
my_set3 = set("11111222222333344444")
print(my_set3)

#Adding elements to a set

my_set4 = set()

my_set4.add("Cristian")
my_set4.add(30)
my_set4.add("Rio de Janeiro")
my_set4.add("1111222233334444")
print(my_set4)

#Removing an element

my_set4.remove(30) #Remove the exact element, if insert another one, it will bring an error
print( my_set4)

my_set4.discard("Cristian") #Remove the element, but when inserting a wrong element, nothing happen.
my_set4.discard("Banana")
print(my_set4)

my_set.clear() #Removo all elements

my_set4.pop() #remove a rondom element.

print(my_set)
print(my_set4)

#Checkking if an element is in Set and also iterating

set1 = {"Monday", "Tuesday", "Wednesday","Thursday", "Friday", "Saturday", "Sunday"}

for i in set1:
    print(i)
if "Monday" in set1:
    print("Yes")
else:
    print("No")


#Union and Intersections

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

un_set = odds.union(evens) # Combine elements from both sets
print(un_set)

#Take elements that are in both set
in_set = odds.intersection(evens)
print(in_set)

in_set = odds.intersection(primes) 
print(in_set)

in_set = evens.intersection(primes)
print(in_set)

#Difference of Sets

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff_set = setA.difference(setB) #Returns a set with all the elements from the setA that aren't in setB
print(diff_set)

diff_set = setB.difference(setA) #Returns a set with all the elements from the setB that aren't in setA
print(diff_set)

diff_set = setA.symmetric_difference(setB) #Returns all elements that are in SetA and setB without elements that are in both.
print(diff_set)

diff_set = setB.symmetric_difference(setA) #This set is eual setA.symetric_difference(setB)
print(diff_set)

#Useful methods to update a Set

setA.update(setB) #Update the set by adding elements from another set

setA.intersection_update(setB) # Update the set by keeping only the elements found in both

setA.difference_update(setB) # Update the set by removing the elements found in another set.

setA.symmetric_difference_update(setB) # Update the set by only keeping the elements found in either set, but not in both.


#Frozenset is just an immutable version of normal set.

a = frozenset([0, 1, 2, 3, 4])

