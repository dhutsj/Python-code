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
