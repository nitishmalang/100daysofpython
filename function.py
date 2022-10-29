#def word():
 #   print("Hello world")

#def addNumbers(a , b):
 #   return a + b 

#print(addNumbers(34 , 7))    
  
#print('hello world')  
#def addNumbers(a , b):
 # return a + b
#print(addNumbers(a = 20 , b =40))  
#def subtractNumber(a = 20 , b = 10):
 #   return a - b
#print(subtractNumber())    

#print(subtractNumber(a = 70))
#print(subtractNumber(b = 9))
#print(subtractNumber(20 , 10))
#def ValueOfList(valuesList = None):
 #   if valuesList is None:
  #     valuesList = []
   #    valuesList.append("Values")
    #   print(valuesList)

#def add(*args):
 # sum = 0
  #for a in args:
   # sum +=a
    #return sum
#add(11,22,33,44,55)

#def printkeyword(**kwargs):
 #  print(kwargs)
#printkeyword(a = 15 , b = 12 , c =16)
#sum = lambda x:x+2 
#print(sum(5))   

#product = lambda x,y:x*y
#print(product(3 , 7))

from itertools import product


def valuesLambda(vals):
  return lambda a:a*vals

  productDouble = valuesLambda(2)
  print(productDouble(11))
def valuesLambda(vals):
  return lambda a : a*vals

  productDouble = valuesLambda(2)
  print(productDouble(11))
  
