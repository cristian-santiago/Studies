#Python itertols modele is a collection of tools for handling iterators.

#Product() can compute the cartesian product of input iterables.
from itertools import accumulate, groupby, product, permutations, combinations, combinations_with_replacement, count, cycle, repeat
import operator

prd = product([10, 20], [30, 40]) # it can be included a repetition, repeat = number
print(list(prd)) #converting iterator to a list for printing.

#Permutations()  can return successive length permutations of elements in an iterable.

perm = permutations(["a", "b", "c"])
#It's possible to change the lenght of the permutation tuples, it must be always < than the max elements.
perm2 = permutations(["a","b","c"], 2) 
print(list(perm))
print(list(perm2))

#Combinations() and combinations_with_replacemement() 
#the second argument is mandatory and specifies the length of the output
cmb = combinations([1, 2, 3, 4], 2) 
print(list(cmb))

cmb2 = combinations_with_replacement([1, 2, 3, 4], 2)
print(list(cmb2))

#Accumulate() make an iterator that returns accumulated sums, or accumulated results.

acc = accumulate([10, 20, 30, 40])
print(list(acc))

acc2 = accumulate([10, 20, 30, 40], func=operator.mul)
print(list(acc2))

acc3 = accumulate([1, 5, 7, 3, 2, 2, 9, 8, 4], func=max)
print(list(acc3))

#Groupby make an iterator that returns consecutive keys and groups from the iterable.
#Use functions or lambda for better resolution

gpb = groupby([1, 2, 3, 4 , 5], key= lambda x: x < 3)
for key, group in gpb:
    print(key, list(group))

gpb2 = groupby(["Hi", "hello", "how are you", "What is it?", "Are you ok?"], key=lambda x: "h" in x )
for key, group in gpb2:
    print(key, list(group))

#Infinite iteratos : count(), cycle(), repeat()

#Count() will initiate a counting by the number inserted
for i in count(10):
    print(i)
    if i>= 20:
        break
print("")

#Cycle() Repeat the elements and return to begining during a cycle;

sum = 0
for i in cycle([1, 2, 3]):
    print(i)
    sum += i
    if sum >= 15:
        break
print("")

#Repeat() is used to repeat the elements inside it;
for i in repeat("C", 5):
    print(i)