import functools

#Decorators with and without arguments

def myDecorator(func):
    @functools.wraps(func)
    def functionThatRunsFun():
        print("In the decorator!!")
        func()
        print("After the decorator!")
    return functionThatRunsFun

@myDecorator
def myFunction():
    print("I am the function!")

myFunction()

# When you call myFunction ... you pass myFunction into myDecorator. Then
# you return functionThatRunsFun and that returned function replaces myFunction.
# Because it replaced myFunction ... myFunction() essentially runs whatever
# is in 'functionThatRunsFun'


## More Complex Decorators: ##

def decoratorWithArgs(number):
    def myDecorator(func):
        @functools.wraps(func)
        def functionThatRunsFunc(*args):
            print("In decorator")
            func(*args)
            print("After the decorator")
        return functionThatRunsFunc
    return myDecorator

@decoratorWithArgs(56)
def myFunctionToo(x , y):
    print(x + y)

myFunctionToo(50 , 50)