#set of colours
colours = {'Pink','Blue','Green','White','Black'}
print(colours)
#add and remove colour
colours.remove('Green')
colours.add('Purple')
print('Update Set of Colours: ', colours)
#Create another set & interset , union
colours2 = {'Pink','Blue','Green'}
#intersection
print('Intersection:', colours.intersection(colours2))
#union
print('Union:', colours.union(colours2))
#difference
print('Difference: ', colours.difference(colours2))
#Check Colour
print('Is Red in set?','Red' in colours)

#convert list with duplicates to set
fruit_list = ['Apple','Grapes','Apple','Mango', 'Grapes']
unique_fruits = set(fruit_list)
print('Unique fruits:' , unique_fruits)