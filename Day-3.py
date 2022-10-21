if True:
    print('Conditional was True')
if False:
    print('Conditional was True')    

language = 'python' #Java
if language == 'Python':
    print("Condition was true ")
elif language == 'Java':  
    print('Language is java')
elif language == 'Javascript':
   print('Lanaguage is javascript')    

else:
    print("no match")    

from operator import truediv


user = 'admin'
logged_in = False #False
if user == 'admin' and logged_in:
if user == 'admin' or logged_in:    
    print('admin page')
else:
    print('Bad credentials')    
if not logged_in:
   print('Please log in')
else:
    print('welcome')    
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
print(id(a))
print(id(b))
a = [1, 2, 3]
b = a
print(id(a))
print(id(b))
print(a is b)
condition = None
condition = 'Test'
if condition:
    print('evaluated to True:')
else:
    print('evaluated to False:')    
