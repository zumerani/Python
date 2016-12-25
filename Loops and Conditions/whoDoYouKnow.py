def whoDoYouKnow():
    people = input("Enter people you know separatd by commas:")
    knownList = people.split(",")
    noSpaces = []
    for i in knownList:
        noSpaces.append( i.strip() ) #Using 'strip' to take out extra white spaces incase user inputs with spaces

    return noSpaces

def askUser():
    list = whoDoYouKnow()
    person = input("Enter the name of a person: ")
    if person in list:
        print( "You know the person: {}!".format(person) )
    else:
        print( "You don't know the person: {}!".format(person) )


askUser()
