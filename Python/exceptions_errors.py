#Exceptions end erros can help to understand the issue related to a code.

#Syntax Error 

# a = 4 print(a) <---> this code will give a SyntaxError, indicating that's a wrong way to code

#Raising an Exceptions
'''
x = -2
if x < 0:
    raise Exception("X should not be negative.")

'''
#Assert 
'''
a = -5
assert (a >=0), "a is not positive"
'''
#Handling Exceptions

#In this case, will bring the msg from except condition;
'''try:
    a = 5 / 0
except:
    print("An error occured.")
'''
#Using Exception to display the error occured.
'''try:
    a = 5/0
except Exception as e:
    print(e)'''

#Using finally to  display something after en error occurred.

'''try:
    a = 5/0
except Exception as e:
    print(e)
finally:
    print("Cleaning up some stuff...")

    '''
#Creating an exeption

class ValueHigh(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

class ValueLow(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value
def test_value(a):
    if a > 100:
        raise ValueHigh("The value is too high.", a)
    if a < 10:
        raise ValueLow("The value is too low.", a)
    return a

try:
    test_value(101)
except ValueHigh as vh:
    print(f"{vh.message} The value is {vh.value}")
except ValueLow as vl:
    print(f"{vl.message} The value is {vl.value}")