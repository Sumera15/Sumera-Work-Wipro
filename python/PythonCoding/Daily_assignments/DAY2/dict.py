#Dictonary operations
print('dictionary operations')

human = {'name': 'Sumera','age':'21','hobby':'reading books'}
print('Dict:',human)
#Acess value
print('name:', human['name'])
#add and update
human['fav_food'] = 'Dosa'
human['hobby'] = 'Dance'
print('updated dic:',human)

#print keys & values
print('keys:', human.keys())
print('values:',human.values())

#remove age
human.pop('age')
print('After removing age:', human)