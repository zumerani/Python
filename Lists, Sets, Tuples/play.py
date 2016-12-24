#Lists, Tuples, and Sets

#Lists -- most flexible
grades = [77, 80, 90, 95, 100]

print( sum(grades) / len(grades) ) #Average

grades.append(108) #Adding item at the end

#Tuple -- Tuples are immutable ... lists are mutable
tuple_grades = (77, 80, 90, 95)

tuple_grades = tuple_grades + (100,) #You can change the uple entirely. If one element, keep the comma.
print(tuple_grades)


#Sets -- Unique and unordered.
set_grades = {77, 80, 90, 100, 100}

set_grades.add(23)
print(set_grades) #Printing it won't print it in order^ It's random

# Sets do not allow assignments (set_grades[0] = x )


#Some more Set Operations:
set_one = {1 , 2 , 3 , 4 , 5}
set_two = {1 , 3 , 5 , 7 , 9 , 11}

print( set_one.intersection(set_two)) #Prints the intersection and returns a set of intersecting values
print( set_one.union(set_two)) #Adds the sets together -- Returns a set with all the elements from both sets (no duplicates)
                               #It first adds set_one and then goes through set_two and checks for duplicates

print( {1 , 2 , 3 , 4}.difference({1 , 2})) #Prints {3 , 4}








