person = {'name': 'Jenn' , 'age':23}

#l =  ['Jenn', 23]
#sentence = 'My name is {0} and Im {1}  years old.'.format(person['name'] , person['age'])
#print(sentence)

#for i in range(1, 11):
 #   sentence = 'The value is {:02}'.format(i)
  #  print(sentence)

#pi = 3.14159265

#sentence = 'Pi is equal to {:.2f}'.format(pi)
#print(sentence)

#sentence = '1MB is equal to {:,.2f} bytes'.format(1000**2)
#print(sentence)

import datetime
my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)

#print(my_date)

sentence = '{0:%B %d , %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)







