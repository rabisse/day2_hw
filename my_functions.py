# #defining function
# def greet():
#     print("Hello")
# greet() #prints Hello


# def greet():
#     return "Hello"
# greeting = greet() #declares variable that uses function as definition
# print(greeting)


# def greet():
#     print("Hello")
# greeting = greet()
# print(greeting)
# #'None' get printed because nothing was 'returned' from the function, so the variable is basically empty


def greet(name, time_of_day): #note the parameter
  return "Good " + time_of_day + " " + name

greeting = greet("Alex", "evening") #note the argument
print(greeting)
#=> Good evening Alex


