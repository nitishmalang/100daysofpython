x = 'global x'

def test(z):
    x = 'local x'
    print(y)
    print(z)

test('local z')
print(x)    
import builtins 

print(dir(builtins))
m = min([5, 1, 4, 2, 3])
print(m)
x = 'global x'

def outer():
    #x = 'outer x'
    def inner():
       # nonlocal x
       # x = 'inner x'
        print(x)

    inner()
    print(x)

outer()
print(x)
