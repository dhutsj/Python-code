import base64

ms = "xxxxx"
ms = ms.encode(encoding='utf-8', errors='strict')
my_password_encode = base64.b64encode(ms)

print('after encode: {}'.format(my_password_encode))
enstr = base64.b64decode(my_password_encode.decode())
print(enstr.decode())
