### 1. 写在前面  ###

在介绍python装饰器之前，首先介绍python的一个概念，对象。在python里，所有的一切皆对象。常用的python对象有整型对象，浮点型对象，字符串对象，列表对象，元组对象，字典对象等。其中一个比较特殊的对象是函数对象。

    num1 = 1         # 定义了一个整型对象，num1引用了这个对象
    str1 = "aaa"     # 定义了一个字符串对象，str1引用了这个对象
    list1 = [1,2,3]  # 定义了一个列表对象，list1引用了这个对象
    
    def my_func()             # 定义了一个函数对象
        print "hello world"   
    func1 = my_func           # func1引用了这个函数对象

以一个普通函数为例。
    
    def my_func(name):
        return "name is {}".format(name)

这里我们定义了一个名为my_func的函数，传入一个字符串对象作为函数的参数，然后返回另一个字符串对象。在上面已经介绍过了，在python中，一切皆对象。那如果我们把一个函数对象作为参数传入，然后返回另一个函数会怎么样呢？这就是装饰器了。


### 2. 基础装饰器  ###

接着上面的疑问，我们写一个这样的函数。
    
    def add(a, b):        # 定义了一个函数对象
        return a + b
    
    myadd = add           # myadd引用了这个函数对象

    def decorator1(func):               # 定义了一个函数对象decorator1，所需参数也是一个函数对象
        def log(*args, **kwargs):       # 在函数内又定义了一个新的函数对象log
            return func(*args, **kwargs)
        return log                      # 返回这个log函数对象
    
    mydecorator = decorator1(myadd)     # 调用函数decorator1，并将myadd作为参数传入，同时将返回的对象赋值给mydecorator, 可知，这里返回的是log函数，
                                        # 也就是说，此时mydecorator指向了log函数
    
    print mydecorator(1, 2)             # 调用mydecorator函数，即调用内部的log函数

来看一下这段代码的执行结果
    
    C:\Python>python mydecorator1.py
    3

我们可以看到它的执行结果就是3，你也许会问写了这么多，不就是两个数的求和吗？不就是上面的add函数吗？上面的代码只是便于让大家理解，如果我们在内部的log函数里加一些操作会怎么样呢？比如打印日志。

    def add(a, b):
        return a + b
    myadd = add
    def minus(a, b):
        return a - b
    myminus = minus
    def decorator1(func):
        def log(*args, **kwargs):
            # do some things here, for example, add some log
            print "function {} was called".format(func.__name__)
            return func(*args, **kwargs)
        return log
    mydecorator1 = decorator1(myadd)
    mydecorator2 = decorator1(myminus)
    print mydecorator1(1, 2)
    print mydecorator2(3, 4)

再来看一下这段代码的执行结果

    C:\Python>python mydecorator1.py
    function add was called
    3
    function minus was called
    -1

我们只需修改内部log函数这一个地方，就可以实现扩充函数的功能，并且这个功能可以应用于多个函数。这就是装饰器最大的意义。这里我是以添加日志为例的，在实际工作中，比如写一个判断是否需要登录操作的装饰器等。


### 3. python装饰器语法糖  ###
在python的实际工作中，通常使用@符号来调用装饰器，称之为python语法糖。
    
    def decorator1(func):
        def log(*args, **kwargs):
            # do some things here, for example, add some log
            print "function {} was called".format(func.__name__)
            return func(*args, **kwargs)
        return log

     @decorator1
     def add(a, b):      # 此时 add = decorator1(add)，add函数就被装饰了
         return a + b
     
     @decorator1
     def minus(a, b):    # 此时 minus = decorator1(minus)，minus函数被装饰了
         return a - b

     print add(1,2)      # 执行装饰好的add函数，而不再是原来的add函数
     print minus(3,4)    # 执行装饰好的minus函数，而不再是原来的minus函数


### 4. 装饰器进阶  ###

上面介绍了基础的装饰器，下面再介绍一些装饰器的进阶用法。

#### 4.1 带参数的装饰器  ####

在上面的例子中，我们可以看到被装饰的函数add，minus是带参数的，但是装饰器decorator1本身除了func这个参数外，是不能带有其他参数的。有没有方法能让装饰器带其他参数呢？比如字符串参数等。答案是可以的，只需要在最外层再封装一个函数即可。
    
    def decorator2(mystring):
        print mystring
        def decorator1(func):
            def log(*args, **kwargs):
                # do some things here, for example, add some log
                print "function {} was called".format(func.__name__)
                return func(*args, **kwargs)
            return log
        return decorator1

    @decorator2("Used decorator here")
    def add(a, b):
        return a + b

    @decorator2("Used decorator here")
    def minus(a, b):
        return a - b

    print add(1,2)
    print minus(3,4)


我们来看这段代码的执行结果

    C:\Python>python mydecorator1.py
    Used decorator here
    Used decorator here
    function add was called
    3
    function minus was called
    -1

#### 4.2 多重装饰  ####

截至目前，我们都只使用了一个装饰器，如果适用多个装饰器效果会怎么样呢？

    from functools import wraps
    
    def decorator1(func):
        @wraps(func)
        def log(*args, **kwargs):
            # do some things here, for example, add some log
            print "function {} was called in decorator1".format(func.__name__)
            return func(*args, **kwargs)
        return log
    
    def decorator2(func):
        @wraps(func)
        def another_log(*args, **kwargs):
            # do some things here, for example, add some log
            print "function {} was called in decorator2".format(func.__name__)
            return func(*args, **kwargs)
        return another_log
    
    @decorator1
    @decorator2
    def add(a, b):
        return a + b
    add(1, 2)

    @decorator2
    @decorator1
    def minus(a, b):
        return a - b
    minus(3, 4)

我们来看这段代码的执行结果
    
    C:\Python>python mydecorator1.py
    function add was called in decorator1
    function add was called in decorator2
    function minus was called in decorator2
    function minus was called in decorator1


### 5. 装饰器总结  ###

1. 装饰器是一个接收函数对象，并且返回一个新的函数对象的函数。
2. 装饰器可以在不修改被装饰函数的情况下，实现代码功能的扩充，而不需要重写或者重构代码。
3. 装饰器通常可以用来添加扩充的日志，判断用户某个操作是否需要登录，是否合法等。
4. 装饰器本身也可以带所需的额外参数。
5. 对于多重装饰，装饰的顺序为装饰器的调用顺序。

