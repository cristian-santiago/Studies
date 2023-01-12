import os
 
RAIZ = os.path.dirname(os.path.realpath(__file__))
database = os.path.join(RAIZ,'banco.db')
print(database)