courses = ['History', 'Math' , 'Physics', 'CompSci']
courses_2 = ['Art' , 'Education']
nums = [1 , 5 , 3 , 4 , 6, 2]
courses.append('Art')
courses.insert(0 , courses_2)
print(courses[0])

print(len(courses))
print(courses[-1])
print(courses[:2])
print(courses[2:])
courses.extend(courses_2)
courses.remove('Math')
popped = courses.pop()
print(popped)
courses.reverse()
courses.sort(reverse=True)
nums.sort(reverse=True)
print(nums)
print(courses)
print(max(nums))
for item in courses:
  print(item)
for course in courses:
for index , course in enumerate(courses, start=1):
    print(index ,  course)

course_str = ' - '.join(courses)
new_list = course_str.split(' - ')
print(course_str)
print(new_list)
  print(course)
  #mutable
list_1 = ['History' , 'Math' , 'Physics' , 'CompSci']
list_2 = list_1
list_1[0] = 'Art'
print(list_1)
print(list_2)
#immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1
tuple_1[0] = 'Art'
print(tuple_1)
print(tuple_2)

#sets
cs_courses = {'History', 'Math' , 'Physics', 'CompSci', 'Math'}
art_courses = {'History', 'Math' , 'Art' , 'Design'}
print('Math' in cs_courses)
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))
print(cs_courses)
