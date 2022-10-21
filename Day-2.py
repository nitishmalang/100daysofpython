student = {'name':'John', 'age':25 , 'courses':['Math' , 'CompSci']}
student['phone'] = '55-555'
student['name'] = 'Jane'
student.update({'name': 'jane' , 'age':'26', 'phone' : '555555'})
del student['age']
age = student.pop('age')
print(student)
print(age)
print(student['name'])
print(student['courses'])
print(student.get('phone'))
print(student.get('phone' , 'Not_Found'))
print(len(student))
print(student.values())
print(student.items())
for key in student:
  print(key)
for key, value in student.items():
    print(key, value)
