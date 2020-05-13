def fib(num):
    a = 0
    b = 1
    count = 1
    while count <= num:
         a, b = a + b, a
         count = count + 1
    yield a

aaa = fib(3)
print type(aaa)

for i in range(5):
    print r"fib({}): {}".format(i, next(fib(i)))
