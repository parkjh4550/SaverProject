#test file : add comment
a = [1,2,3,4]
b = a
b[0] = 4
print('a : ', a)
print('b : ', b)
print('id(a) : ', id(a))
print('id(b) : ', id(b))

a = [1,2,3,4]
b = a[:]
b[0] = 4
print('a : ', a)
print('b : ', b)
print('id(a) : ', id(a))
print('id(b) : ', id(b))

for i in range(1,11):
    print(i)

