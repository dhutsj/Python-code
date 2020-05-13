def reverse_string(string):
    l1 = list(string)
    for i in range(len(l1)//2):
        l1[i], l1[len(l1) - i - 1] = l1[len(l1) - i - 1], l1[i]
    return ''.join(l1)


def reverse_string1(string):
    return string[::-1]


def reverse_string2(string):
    rev_string = ''
    for i in range(len(string)-1, -1, -1):
        rev_string += string[i]
    return rev_string


print reverse_string('abcdefg')
print reverse_string1('abcdefg')
print reverse_string2('abcdefg')
