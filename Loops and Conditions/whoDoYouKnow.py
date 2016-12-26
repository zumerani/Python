def whoDoYouKnow():
    people = input("Enter people you know separated by commas:")
    #knownList = people.split(",")
    #noSpaces = []
    #for i in knownList:
    #    noSpaces.append( i.strip() ) #Using 'strip' to take out extra white spaces incase user inputs with spaces

    #Rather than doing the above code^, we can do this:
    noSpaces= [ person.strip() for person in people.split(",") ] #grabs the list with ',' delimeter and strips each word
    print("noSpaces is: {}".format(noSpaces))

    return noSpaces

    #To make the function a one-liner, we can also do this:
    #return [ person.strip() for person in input("Enter people you know separated by commas: ").split(",") ]

def askUser():
    list = whoDoYouKnow()
    person = input("Enter the name of a person: ")
    if person in list:
        print( "You know the person: {}!".format(person) )
    else:
        print( "You don't know the person: {}!".format(person) )


askUser()
