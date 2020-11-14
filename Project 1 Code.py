import csv

filename = "students.csv"

with open(filename) as csvfile:
   reader = csv.DictReader(csvfile)
   student_id = input('Enter the student id: ')
   for row in reader:
       if student_id == row['student_id']:
           for key,value in row.items():
               print(key,':',value)
           break
   else:
       print('This id does not exist')