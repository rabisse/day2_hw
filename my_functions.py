#defining function
def greet():
    print("Hello")
greet() #prints Hello


def greet():
    return "Hello"
greeting = greet() #declares variable that uses function as definition
print(greeting)
