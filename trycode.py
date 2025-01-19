  # A simple decorator function
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

''' A simple decorator function
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