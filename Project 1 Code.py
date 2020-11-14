import csv

def main():

    while True:
        meun()
        choice = int(input('Plese select\n'))
        if choice in [1,2,3,]:
            if choice == 1:
                student_inform()
                break

            elif choice == 2:
                course()

            elif choice == 3:
                change()
                break

def student_inform():       #create a definition of student inform.
    filename = "Students.csv"       #then I set the filename connect with the 1 database that I created [Students]

    with open(filename,'r') as csvfile:     #So, I learn the 'with' statement from zybook on 10.6, open the file as csv, just for reading it
       reader = csv.DictReader(csvfile)     #an function that can read csv file as dictionary.
       student_id = input('Enter the student id: ')     #Enter the student id as a keyword
       for row in reader:       #create a for loop to find if this id is in csv file.
           if student_id == row['student_id']:      #if is found
               for key,value in row.items():        #if the key[id] is found in the csv file.
                   print(key,':',value)     #print down the id of that, and write it as rows
               break        #finish the loop
       else:
           print('This id does not exist')      #else, since the id is not in my database, so 'this does not exist'


def meun():
    print("----------------meun--------------------")
    print("|         1.Student information        |")
    print("|         2.Courses                    |")
    print("|         3.Change                     |")
    print("----------------------------------------")


def course():
    with open('Student_courses.csv', 'r') as gradefile:
        read = csv.DictReader(gradefile)
        student_id = input('Enter the student number: ')
        for row in read:
            if student_id == row['student_id']:
                for key, value in row.items():
                    print(key, ':', value)
                break

            else:
                print('This number does not exist')

def change():
    print()

if __name__ == '__main__':
    main()
