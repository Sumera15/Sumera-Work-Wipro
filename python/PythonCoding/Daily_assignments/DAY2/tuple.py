#Creat a tuple
print('Three Places to visit: ')
cities = ('Jaipur','Goa','Kerala')
print(cities)

#Acess and print first & last place
print('First City: ',cities[0])
print('Last City: ',cities[2])

#Concatenate two tuples
cities2 = ('Delhi','Vizag')
allcities = cities + cities2
print(allcities)
#Trying changing element
'''try:
    cities[0] = "Berlin"
except TypeError as e:
    print("Error"("Tuples are immutable"))'''

#Unpack the elements
c1, c2, c3 , c4,c5 = allcities
print(c1, c2, c3,c4,c5)
