from unicodedata import name


#def hello_func(greeting, name = 'you'):
 #   return 'Hello Function.'.format(greeting, name)

#print(hello_func())

#print(len('Test'))
#print(hello_func().upper())
#print(hello_func('Hi', name= 'Corey'))

def student_info(*args , **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'John', 'age' : 22 }    
#student_info('Math', 'Art', name = 'John' , age = 22)    

student_info(*courses , **info)