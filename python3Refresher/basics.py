from random import randrange, randint

# variables
fName = input("Your first name: ") # Example for string variable
lName = input("Your last name: ")

# How to accept multiple inputs in a line
# In the below line map() is to convert the input into specific datatype; 
a,b,c = map(int, input("Enter your 3 inputs in 1 line: ").split()) # This line accepts 3 inputs
print(a,b,c)



# print function to display the output to the screen
print("Hello,"  + fName + ' ' + lName + '.' + " Let's learn Python & Django")

age = float(input("What is your age? ")) # Example for float variable

if age>18:
    major = True
else:
    major = False

# Data Types in Python - List [], Tuple (), Set {}, Dictionary {key:value}

# List [] is a collection of objects which are ordered, mutable and also allow duplicates
exList = [fName,lName,age,1988]
print(exList)
# Tuple () is a collection of objects which are ordered, immutable and also allow duplicates
exTuple = (fName,lName,age,1988,exList)
print(exTuple)
# Set {} is a collection of objects which are Unordered, immutable and also don't allow duplicates
exSet = {1,fName,2,lName,3,age}
print(exSet)
# Dictionary {key:value} is a collection of key: value pairs which are Unordered, mutable and also don't allow duplicates
exDictionary = {'FistName': fName, 'LastName':lName, 'Age': age}
print(exDictionary)

# Example for conditional statement

if age < 5:
    print("You are too young to learn coding...!")
elif (age > 5) and (age < 10):
    print("You can start learning coding but it is advised to wait till you become 10..!")
else:
    print("You can learn coding...!!")

# Example for while loop

score = 0
totalScore = 0
balls = 0
wkt = False
while (balls >= 0):
    balls += 1
    wkt = randint(0,1)
    if wkt == True:
        if (balls == 1) and (totalScore == 0):
            print("Number of balls played: "+str(balls))
            print("Scored: "+ str(score))
            print("Duckout!!")
        break
    else:
        score = randrange(0,7)
        print("Scored: "+ str(score))
        print("Ball: "+ str(balls))
        totalScore += score
        print("Number of balls played: "+str(balls))
print("Your total score is: "+ str(totalScore)+" runs")

# for loop example
num = list()
for i in range(100):
    num.append(i)
print(num)

# Data-Type Methods
print(fName.capitalize())
print(fName.casefold())
print(fName.upper())
print(fName.lower())
print(fName.rpartition('k',))
print(fName.title() == fName.capitalize())
print((fName+lName).count('i'))
print((fName+lName).index('i'))

# len() function
print(len(fName))
print(len(exList))
print(len(exTuple))
print(len(exSet))
print(len(exDictionary))

''' ----------- Data Type Methods--------------'''
# List Methods
exList.append('Pranuthi') # append() works on list since it is mutable. 
exList.insert(0,'Vivaan') # insert() is to add an element in the specified index
exList.extend(exTuple) # extend() will add iterable items (list, set, tuple e.t.c) to the existing list
exList.pop() # pop() will remove an element in the specified index, if index isn't specified it'll remove the last element
exList.remove('Pranuthi') # remove() will delete first existance  of the specified value
exList.clear() # clear() will remove all elements in the list

# Set Methods
''' Union, Intersection, Difference, Symmetric Difference'''
# Add() method is to add an object to the set
setPets = {'parrots', 'monkeys', 'tigers', 'lions'}
setPets.add('sparrows')
print(setPets)
setPetsB = setPets.add('Tigers')
# Intersection
print(setPetsB.intersection(setPets)) # revisit this line again to sort the issue.













    
    
    
   
    
        




