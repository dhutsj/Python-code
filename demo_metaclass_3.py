z = type('Z', (), {"name": "tsj", "age": 20})
z.place = "Shanghai"
print(type(z))
print(z.place)

def my_metaclass(name, parents, attr):
    return type(name, parents, attr)

z = my_metaclass('Z', (), {"name": "tsj", "age": 20})
print(type(z))
print(z.name)

class Z():
    def __init__(self, name):
        self.name = name

z = Z("tsj")
print(type(z))
print(type(type(z)))

class My_Metaclass(type):
    def __new__(cls, name, parents, attr):
        print("Call new method.")
        return type.__new__(cls, name, parents, attr)

z = My_Metaclass("Z", (), {"name": "tsj"})
print(z.name)

class A(object): 
    def __new__(cls): 
         print("Creating instance") 
         return super(A, cls).__new__(cls) 
  
    def __init__(self): 
        print("Init is called") 
  
a = A()
