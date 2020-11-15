import csv

def main():

    while True:
        meun()
        choice = int(input('Plese select\n'))
        if choice in [1,2,3,4,5]:
            if choice == 1:
                student_inform()
                break

            elif choice == 2:
                read_ids()

            elif choice == 3:
                break
            elif choice == 4:
                change_student_courses()
            elif choice == 5:
                break

def meun():
    print("----------------meun--------------------")
    print("|         1.Student information        |")
    print("|         2.Courses                    |")
    print("|         3.Change inform              |")
    print("|         4.Change courses             |")
    print("|         5.Exit                       |")
    print("----------------------------------------")

def student_inform():       #this is a system for part1
    filename = "Students.csv"

    with open(filename) as csvfile:
       reader = csv.DictReader(csvfile)
       student_id = input('Enter the student id: ')
       print('○○○○○○○○○○○○○○○○○○○○○○○○○')
       for row in reader:
           if student_id == row['student_id']:
               for key,value in row.items():
                   print(key,':',value)
               break
       else:
           print('This id does not exist')
       print('○○○○○○○○○○○○○○○○○○○○○○○○○')
       while True:
           meun()
           choice = int(input('Plese select\n'))
           if choice in [1, 2, 3, ]:
               if choice == 1:
                   student_inform()
                   break

               elif choice == 2:
                   read_ids()

               elif choice == 3:
                   break
               elif choice == 4:
                   change_student_courses()
               elif choice == 5:
                   break

#---------------------------------------------------------------------------------------------
#this is the system for part 2
import webbrowser

student0 = ['student_id\n',     #example for student form
               '2020, Fall, CMPSC131 100 100 100 100 \n'
               '2020, Fall, MATH140 100 100 100 100 \n'
               '2020, Fall, ENGL015 100 100 100 100 \n'
               '2020, Fall, KINES101 100 100 100 100 \n'
               '2020, Fall, PSU001 100 100 100 100 \n'
               '2020, Fall, COMM100 100 100 100 100 \n'
               ]
#I deleted all others, and decide to put it in all different database

def student0_course():       #this is just an example of how the other 15 works
        with open('database.txt','w+') as gradefile:
            read = gradefile.readlines()
            gradefile.write(student0[0])
            gradefile.writelines(student0[1])
            gradefile.close()

def student1_course():
    f = open("database1.txt", "r")
    print(f.read())
    f.close()
    
def student2_course():
    f = open("database2.txt", "r")
    print(f.read())
    f.close()
    
def student3_course():
    f = open("database3.txt", "r")
    print(f.read())
    f.close()

def student4_course():
    f = open("database4.txt", "r")
    print(f.read())
    f.close()

def student5_course():
    f = open("database5.txt", "r")
    print(f.read())
    f.close()

def student6_course():
    f = open("database6.txt", "r")
    print(f.read())
    f.close()

def student7_course():
    f = open("database7.txt", "r")
    print(f.read())
    f.close()

def student8_course():
    f = open("database8.txt", "r")
    print(f.read())
    f.close()

def student9_course():
    f = open("database9.txt", "r")
    print(f.read())
    f.close()


def student10_course():
    f = open("database10.txt", "r")
    print(f.read())
    f.close()

def student11_course():
    f = open("database11.txt", "r")
    print(f.read())
    f.close()

def student12_course():
    f = open("database12.txt", "r")
    print(f.read())
    f.close()

def student13_course():
    f = open("database13.txt", "r")
    print(f.read())
    f.close()

def student14_course():
    f = open("database14.txt", "r")
    print(f.read())
    f.close()

def student15_course():
    f = open("database15.txt", "r")
    print(f.read())
    f.close()


def course_datas():
    with open('database.txt', 'r') as gradefile:
        print(webbrowser.open("database.txt"))
        gradefile.close()

#---------------------------------------------------------------------------------------------

def read_ids():     #read all the ids, and open them with notepad
    with open('database.txt', 'r') as gradefile:
        student_id = input('Enter the student number: ')
        if student_id == 'jkl6150':
                student1_course()
        elif student_id =='jmc8444':
                student2_course()
        elif student_id =='abc0003':
                student3_course()
        elif student_id =='abc0004':
                student4_course()
        elif student_id =='abc0005':
                student5_course()
        elif student_id =='abc0006':
                student6_course()
        elif student_id =='abc0007':
                student7_course()
        elif student_id =='abc0008':
                student8_course()
        elif student_id =='abc0009':
                student9_course()
        elif student_id =='abc0010':
                student10_course()
        elif student_id =='abc0011':
                student11_course()
        elif student_id =='abc0012':
                student12_course()
        elif student_id =='abc0013':
                student13_course()
        elif student_id =='abc0014':
                student14_course()
        elif student_id =='abc0015':
                student15_course()
        else:
            print('This student id does not exist')

#---------------------------------------------------------------------------------------------

def change_Student_inform():
    print('○○○○○○○○○○○○○○○○○○○○○○○○○')

def change_student_courses():
    print('○○○○○○○○○○○○○○○○○○○○○○○○○')
    print('You can edit anything by using notepad,')
    print('Format:\nYears,Semaster,Class,Test1,Test2,Test3,Test4\n(IMPORTANT:Remember to save the file!!!)')
    student_id = input('Enter your student id to change your course\n')
    if student_id == 'jkl6150':
        student1_course()
        print('Opening the file....\nPlease Wait')
        course_datas()
        ans = input('Are you finished?')
        if ans == 'Yes':
            with open("database.txt", 'r') as f:
                student1 = [line.rstrip('\n') for line in f]
                print(student1)
    elif student_id == 'jmc8444':
        student2_course()
        print('Opening the file....\nPlease Wait')
        course_datas()
    elif student_id == 'abc0003':
        student3_course()
        print('Opening the file....\nPlease Wait')
        course_datas()
    elif student_id == 'abc0004':
        student4_course()
        print('Opening the file....\nPlease Wait')
        course_datas()
    elif student_id == 'abc0005':
        student5_course()
        print('Opening the file....\nPlease Wait')
        course_datas()
    elif student_id == 'abc0006':
        student6_course()
        print('Opening the file....\nPlease Wait')
        course_datas()
    elif student_id == 'abc0007':
        student7_course()
        print('Opening the file....\nPlease Wait')
        course_datas()
    elif student_id == 'abc0008':
        student8_course()
        print('Opening the file....\nPlease Wait')
        course_datas()
    elif student_id == 'abc0009':
        student9_course()
        print('Opening the file....\nPlease Wait')
        course_datas()
    elif student_id == 'abc0010':
        student10_course()
        print('Opening the file....\nPlease Wait')
        course_datas()
    elif student_id == 'abc0011':
        student11_course()
        print('Opening the file....\nPlease Wait')
        course_datas()
    elif student_id == 'abc0012':
        student12_course()
        print('Opening the file....\nPlease Wait')
        course_datas()
    elif student_id == 'abc0013':
        student13_course()
        print('Opening the file....\nPlease Wait')
        course_datas()
    elif student_id == 'abc0014':
        student14_course()
        print('Opening the file....\nPlease Wait')
        course_datas()
    elif student_id == 'abc0015':
        student15_course()
        print('Opening the file....\nPlease Wait')
        course_datas()
    else:
        print('This student id does not exist')

    print('○○○○○○○○○○○○○○○○○○○○○○○○○')

if __name__ == '__main__':
    main()
