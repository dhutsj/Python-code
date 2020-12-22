def judge_cache(func):
    cache_list = []

    def inner():
        num = func()
        if num in cache_list:
            return "Inputed before, cached"
        else:
            cache_list.append(num)
            return cache_list
    return inner


@judge_cache
def input_num():
    num = input("Please input a int number: " + "\n")
    return num


for i in range(0, 2):
    print(input_num())
