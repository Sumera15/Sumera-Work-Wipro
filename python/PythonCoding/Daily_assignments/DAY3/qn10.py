import os

#print working directory
print(os.getcwd())

#create new directory
os.makedirs('new_folders')

#checking
print(os.path.exists('new_folders'))

#list directory
print(os.listdir())