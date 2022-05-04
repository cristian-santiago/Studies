#Lambda functions are used when a simple function is used only once or for a short period in the code;
# lambda function : expression

# a lambda function that adds 20 to the input argument


f = lambda x: x+20

val_1 = f(5)
print(val_1)

# a lambda function that multiplies two input arguments and return the result

f2 = lambda x ,y: x*y
val_2 = f2(3, 5)
val_3 = f2(5, 10)
print(val_2, val_3)

# Lambda inside another function
def my_func(l):
    return lambda x: x*l

v = my_func(2)
print(v(3))

#Using lambda for map function
#map(func, seq) -> Transforms each element with the function

a  = [1, 2, 3, 4, 5, 6, 7]
b  = list(map(lambda x: x*2, a))

c = [x*2 for x in a ] # Alternative
print(b)
print(c)

#Using lambda for filter function
#filter(func, seq) -> Returns all elements for  which func evaluates to True

a = [1, 2, 3, 4, 5, 6, 8, 9, 10]
b = list(filter(lambda x: (x%2 == 0), a))

c = [x for x in a if x%2 == 0]# Alternative 
print(b)
print(c)

# Using lambda with reduce function
# reduce(func, seq) - repeatedly applies the func to the elements and returns a single value.
# The function takes two arguments

from functools import reduce

a = [1, 2, 3, 4]
prod_a = reduce(lambda x, y: x*y, a)
print(prod_a)
