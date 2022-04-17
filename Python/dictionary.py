#Dictionaries has elements named keys and values

#Two ways to add keys and values to a dictionary
mydict = {"name":"Cristian", "age":30, "city":"Rio de Janeiro"}
print(mydict)

mydict2 = dict(name="Ana", age= 15, city="São Paul")
print(mydict2)

#Looking for a value on dictionary by the key
value = mydict["name"]
print(value)

#Adding keys and values in dictionary is simple
mydict["email"] = "cris@mail.com" 
print(mydict)

#To delete an element, only necessary delet the key
#clear() remove all pairs
del mydict["email"]
print(mydict)

#Conditions and Exeptions with Dictionary
if "age" in mydict:
    print(mydict["age"])
else:
    print("No element inside the dictionary.")

try:
    print(mydict["name"])
except:
    print("Error")
#Iteration on dictionary using For as loop

for key in mydict: #List all keys in a dictionary
    print(key)

for value in mydict.values():#List all values in a dictionary
    print(value)

for key, value in mydict.items():# List both keys and values
    print( key, value)

#Updating a dictionary
dict1 = {"a":1, "b":2, "c":3}
dict2 = {"d":4, "e":5, "f":6}

dict1.update(dict2)
print(dict1)