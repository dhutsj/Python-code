import time

def wrapper(func):
    print "it is a decorator"
    def deco(*args, **kwargs):
       print "{} called {}".format(time.time(), func.func_name)
       begin = time.time()
       result = func(*args, **kwargs)
       end = time.time()
       print "func {} spent {} time".format(func.func_name, end - begin)
       return result
    return deco

@wrapper
def add(a,b):
    return a + b

print add(1,2)

def minus(c,d):
    return c - d

minus = wrapper(minus)
print minus(2,1)
