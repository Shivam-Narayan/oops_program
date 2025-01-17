'''A lambda function is a small anonymous function.
   An anonymous functions means that the function is without a name.
   A lambda function can take any number of arguments, but can only have one expression.
   
   Syntax : lambda arguments : expression'''
#Add 10 to argument a, and return the result:   
x = lambda a : a + 10
print(x(5)) #op 15

#Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
print(x(5, 6))  #op 30 

#Summarize argument a, b, and c and return the result:
x = lambda a, b, c : a + b + c
print(x(5, 6, 2)) #op 13
   
# Example: Check if a number is even or odd
check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(4)) #op Even
print(check(7)) #op odd

# Example: Perform addition and multiplication in a single line
calc = lambda x, y: (x + y, x * y)

res = calc(3, 4)
print(res) #op 7,12

# Example: Filter even numbers from a list
n = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, n)
print(list(even)) #op [2, 4, 6]

# Example: Double each number in a list
a = [1, 2, 3, 4]
b = map(lambda x: x * 2, a)
print(list(b)) #op [2, 4, 6, 8]

#Reduce function.

from functools import reduce

# Example: Find the product of all numbers in a list
a = [1, 2, 3, 4]
b = reduce(lambda x, y: x * y, a)
print(b) #op 24