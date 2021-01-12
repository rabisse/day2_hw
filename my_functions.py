#defining function
def greet():
    print("Hello")
greet() #prints Hello



def greet():
    return "Hello"
greeting = greet() #declares variable that uses function as definition
print(greeting)



def greet():
    print("Hello")
greeting = greet()
print(greeting)
#'None' get printed because nothing was 'returned' from the function, so the variable is basically empty



def greet(name, time_of_day): #note the parameter
  return "Good " + time_of_day + " " + name

greeting = greet("Alex", "evening") #note the argument
print(greeting)
#=> Good evening Alex



def greet(name, time_of_day): #note the parameter
  return "Good " + time_of_day + " " + name

name_1 = "Frank"
time_of_day = "afternoon"
greeting = greet(name_1, time_of_day) #variables as arguments
print(greeting)
#=> Good afternoon Frank



#a function that can take different lists and return the total eggs collected
chickens = [
  { "name": "Margaret", "age": 2, "eggs": 0 },
  { "name": "Hetty", "age": 1, "eggs": 2 },
  { "name": "Henrietta", "age": 3, "eggs": 1 },
  { "name": "Audrey", "age": 2, "eggs": 0 },
  { "name": "Mabel", "age": 5, "eggs": 1 },
]

def count_eggs( list ):
    total_eggs = 0

    for bird in list:
        total_eggs += bird["eggs"]
        bird["eggs"] = 0 # eggs have been collected

    return f"{total_eggs} eggs collected"

print(count_eggs(chickens))

