nums = [1,2,3,4,5,6,7,8]

#my_list = [n for n in nums]

# I want 'n*n' for each 'n' in nums
#my_list = []
#for n in nums:
 #   my_list.append(n*n)


#my_list = [n*n for n in nums]

# using a map + lambda
#my_list = map(lambda n: n*n, nums)
#my_list = [n for n in nums if n%2 == 0]
#
#using filter lambda
#my_list = filter(lambda n: n%2 == 0, nums)
#print(my_list)

#I want a (letter , num) pair for each letter
#my_list = []
#for letter in 'abcd':
 #   for num in range(4):
  #      my_list.append((letter,num))
#print(my_list)

#my_list = [(letter , num) for letter in 'abcd' for num in range(4)]
#print(my_list)

# dictionary Comprehensions
names = ['Bruce', 'Clark' , 'Peter' , 'Logan' , 'Wade']
heros = ['Batman', 'Superman', 'Spiderman' , 'Wolverine' , 'Deadpool']
#print(zip(names, heros))
# I want a dict {'name':'hero'} for each name,hero in zip(names , heros)
#my_dict = {}
# for name, hero in zip(names, heros):
 #   my_dict[name] = hero
#print(my_dict)

my_dict = {name: hero for name, hero in zip(names , heros) if name != 'Peter'}  
#print(my_dict)
#set 
#nums = [1,1,1,2,3,4,3,4,5,5,6,7,8,7,9,9]
#my_set = set()
#for n in nums:
 
 #   my_set.add(n)
#my_set = {n for n in nums}

#print(my_set)    

#Generator Expressions

nums = [1,2, 3 ,4 ,5, 6, 7, 8 ,9,10]

#def gen_func(nums):
 #   for n in nums:
  #      yield n*n
#my_gen = (n*n for n in nums)


for i in my_gen:
    print(i)        