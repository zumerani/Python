#Iterables and Loops
myString = "Hello"

for i in myString: #myString is an iterable. Iterables are strings, sets, tuples, and lists, etc.
    print(i)

my_list = [1 , 3 , 5 , 7 , 9]
for i in my_list:
    print( i ** 2 ) #i to the power of 2


#Boolean
myBoolean = True
while myBoolean == True:
    userInput = input("Should we print again? (yes/no)") #Note: 'input' is valid only in Python 3.5 not 2.7!
    if userInput == 'no' :
        myBoolean = False


#If Statements (Conditions)
shouldPrint = True
#Both loops below are similar
if shouldPrint == True:
    print("We're good")

if shouldPrint:
    print("We're good too")


people = ['John' , 'Mary' , 'Anne' ]
userInput = input("Enter a name: ")

if userInput in people:
    print( "We found the person: {}".format(userInput) ) #Formatting strings appropriately
else: #don't forget the colon
    print("You do not know this person")

