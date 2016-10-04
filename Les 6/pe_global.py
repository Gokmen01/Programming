x = 42
y = 21
z = 22

def foo(x, y):
    global z

    x *= 2
    y *= 2
    z *= 2
    print('{} {} {}' .format(x, y, z))


print(x,y, z)
foo(x,y)
print(x,y, z)
