from oopconcepts.college import College
from oopconcepts.student import Student
cc = int(input('C Code: '))
cn = input('C Name: ')
ci = input('City: ')
rno = int(input('Roll No: '))
sn = input('Student Name: ')
m1 = int(input('M1: '))
m2 = int(input('M2: '))
m3 = int(input('M3: '))
'''project = College(ccode=cc, cname=cn, ccity =ci)

project.welcome_message()
project.display_college_details()
'''

project = Student(ccode=cc, cname=cn, ccity=ci, rno=rno, sname=sn,m1=m1, m2=m2, m3=m3)
project.welcome_message()
project.display_college_details()
print(f'Roll No: {project.rollno} \t  Name: {project.stuname}'
      f'Total: {project.calculate_total()} \n Average:{project.calculate_average()}')
