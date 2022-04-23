#Collections : Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter, namedtuple, OrderedDict, defaultdict, deque


#Counter 

a = "122333444455555"
b = [9, 8, 0, 5, 5, 5, 8, 5, 1]

my_counter = Counter(a)
my_counter_b = Counter(b)
print(my_counter)
print(my_counter.most_common(1)) # Show only one most common item, if change for 2, will show up 5 and 4
print(list(my_counter_b.elements())) # Return an iterator over elements repeating each as many times.

#namedtuple

points = namedtuple('Point', 'x, y, z')
pt = points(1, 5, -3)
print(pt)
print(pt._fields)
print(type(pt))
print(pt.x, pt.y, pt.z)

#OrderedDict

ordinary_dict = {}

ordinary_dict = OrderedDict()

#defaultdict

d = defaultdict(int)

d['Amarelo'] = 1
d['Azul'] = 2
print(d.items())
print(d['verde'])

#deque

c = deque()

c.append("a")
c.append('b')
print(c)

c.appendleft("c")
print(c)

""" 
Other useful methods with deque

.pop()
.popleft()
.clear
.extend()
.extendleft()
.count()
.rotate()
"""

