'''# A simple decorator function
def decorator(func):
                
    def wrapper():
        print("Transaction initiated..")
        func()
        print("Transaction completed..")
    return wrapper

# Applying the decorator to a function
@decorator

def hello():
    print("...Executing all the steps of Transaction...")
#hello1 = decorator(hello)
hello() 

A simple decorator function
def decorator(func):
  
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

# Applying the decorator to a function
@decorator

def greet():
    print("Hello, World!")

greet()'''
'''try:
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))
    result = a / b
    print('Result is: ', result)
except ZeroDivisionError:
    print('Cannot divide by zero!')
except ValueError:
    print('Please enter valid integers!')
except Exception as e:
    print('An error occurred: ', e)'''
    
mystr = "banana"
myit = iter(mystr)
print(iter(mystr))
'''print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))'''
    