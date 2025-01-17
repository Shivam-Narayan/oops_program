'''Filter function is used to filter items from a collection.
   In other words filter function is used to remove items from collection based on the given condition.
   
   Syntax: filter(function, iterable)
   
   function:	A Function to be run for each item in the iterable
   iterable:	The iterable to be filtered'''
   
#Filter the array, and return a new array with only the values equal to or above 18:
ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)
  
  
  
# Function to check if a number is even
def even(n):
    return n % 2 == 0

a = [1, 2, 3, 4, 5, 6]
b = filter(even, a)

# Convert filter object to a list
print(list(b))  


#Using filter() with lambda
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a)

print(list(b))

#Combining filter() with Other Functions

a = [1, 2, 3, 4, 5, 6]

# First, filter even numbers
b = filter(lambda x: x % 2 == 0, a)

# Then, double the filtered numbers
c = map(lambda x: x * 2, b)

print(list(c))