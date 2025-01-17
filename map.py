'''Map function is used to map/apply the logic on every items present in collection.
   
   Syntax: map(function, iterables)
   
   function: The function to execute for each item.
   iterable: A sequence, collection or an iterator object. You can send as many iterables as you like, 
             just make sure the function has one parameter for each iterable.
'''
   
#Calculate the length of each word in the tuple:
def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))

#Make new fruits by sending two iterable objects into the function:
def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

#map() with lambda
a = [1, 2, 3, 4]

# Using lambda function in "function" parameter
# to double each number in the list
res = list(map(lambda x: x * 2, a))
print(res)

#converting  to uppercase
fruits = ['apple', 'banana', 'cherry']
res = map(str.upper, fruits)
print(list(res))