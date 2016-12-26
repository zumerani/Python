#Iterables and Loops
myString = "Hello"

for i in myString: #myString is an iterable. Iterables are strings, sets, tuples, and lists, etc.
    print(i)

my_list = [1 , 3 , 5 , 7 , 9]
for i in my_list:
    print( i ** 2 ) #i to the power of 2

#Ranges
myList = [ x for x in range(5) ] #generates: [0, 1 , 2 , 3 , 4]

print("myList: {}".format(myList) )

myMutlipleList = [ x * 3 for x in range(3) ] #generates: [0 , 3 , 6]
print("myMultipleList: {}".format( myMutlipleList) )

myModulo = [ x for x in range(10) if x % 2 == 0 ] #generates: [0 , 2 , 4 , 6 , 8]
print( "myModulo is: {}".format( myModulo ) )

#Playing with strings and lists
myPeople = ["Zain" , "ALBERT" , "  Barry" , "Ken" ]
fixedMyPeople = [ person.strip().lower() for person in myPeople ]#generates: ['zain', 'albert', 'barry', 'ken']
print( "fixedMyPeople is: {}".format( fixedMyPeople ) )

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


