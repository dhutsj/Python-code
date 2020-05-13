class MyClass:
    @property
    def a(self):
        print("getter called")
        return self._a

    @a.setter
    def a(self, value):
        self._a = value
        print("setter called")

m = MyClass()
m.a = 123
print(m.a)
