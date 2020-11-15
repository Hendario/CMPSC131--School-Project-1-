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
                read_ids()

            elif choice == 3:
                change()
                break

def meun():
    print("----------------meun--------------------")
    print("|         1.Student information        |")
    print("|         2.Courses                    |")
    print("|         3.Change                     |")
    print("----------------------------------------")

def student_inform():       #this is a system for part1
    filename = "Students.csv"

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

student1 = ['jkl6150\n',
               '2020, Fall, CMPSC131 100 100 100 100 \n'
               '2020, Fall, MATH140 100 100 100 100 \n'
               '2020, Fall, ENGL015 100 100 100 100 \n'
               '2020, Fall, KINES101 100 100 100 100 \n'
               '2020, Fall, PSU001 100 100 100 100 \n'
               '2020, Fall, COMM100 100 100 100 100 \n'
               ]

student2 = ['jmc8444\n',
               '2020, Fall, CMPSC131 100 100 100 100 \n'
               '2020, Fall, MATH140 100 100 100 100 \n'
               '2020, Fall, ENGL015 100 100 100 100 \n'
               '2020, Fall, KINES101 100 100 100 100 \n'
               '2020, Fall, PSU001 100 100 100 100 \n'
               '2020, Fall, COMM100 100 100 100 100 \n'
               ]

student3 = ['abc0003\n',
               '2020, Fall, CMPSC131 100 100 100 100 \n'
               '2020, Fall, MATH140 100 100 100 100 \n'
               '2020, Fall, ENGL015 100 100 100 100 \n'
               '2020, Fall, KINES101 100 100 100 100 \n'
               '2020, Fall, PSU001 100 100 100 100 \n'
               '2020, Fall, COMM100 100 100 100 100 \n'
               ]

student4 = ['abc0004\n',
               '2020, Fall, CMPSC131 100 100 100 100 \n'
               '2020, Fall, MATH140 100 100 100 100 \n'
               '2020, Fall, ENGL015 100 100 100 100 \n'
               '2020, Fall, KINES101 100 100 100 100 \n'
               '2020, Fall, PSU001 100 100 100 100 \n'
               '2020, Fall, COMM100 100 100 100 100 \n'
               ]

student5 = ['abc0005\n',
               '2020, Fall, CMPSC131 100 100 100 100 \n'
               '2020, Fall, MATH140 100 100 100 100 \n'
               '2020, Fall, ENGL015 100 100 100 100 \n'
               '2020, Fall, KINES101 100 100 100 100 \n'
               '2020, Fall, PSU001 100 100 100 100 \n'
               '2020, Fall, COMM100 100 100 100 100 \n'
               ]

student6 = ['abc0006\n',
               '2020, Fall, CMPSC131 100 100 100 100 \n'
               '2020, Fall, MATH140 100 100 100 100 \n'
               '2020, Fall, ENGL015 100 100 100 100 \n'
               '2020, Fall, KINES101 100 100 100 100 \n'
               '2020, Fall, PSU001 100 100 100 100 \n'
               '2020, Fall, COMM100 100 100 100 100 \n'
               ]

student7 = ['abc0007\n',
               '2020, Fall, CMPSC131 100 100 100 100 \n'
               '2020, Fall, MATH140 100 100 100 100 \n'
               '2020, Fall, ENGL015 100 100 100 100 \n'
               '2020, Fall, KINES101 100 100 100 100 \n'
               '2020, Fall, PSU001 100 100 100 100 \n'
               '2020, Fall, COMM100 100 100 100 100 \n'
               ]

student8 = ['abc0008\n',
               '2020, Fall, CMPSC131 100 100 100 100 \n'
               '2020, Fall, MATH140 100 100 100 100 \n'
               '2020, Fall, ENGL015 100 100 100 100 \n'
               '2020, Fall, KINES101 100 100 100 100 \n'
               '2020, Fall, PSU001 100 100 100 100 \n'
               '2020, Fall, COMM100 100 100 100 100 \n'
               ]

student9 = ['abc0009\n',
               '2020, Fall, CMPSC131 100 100 100 100 \n'
               '2020, Fall, MATH140 100 100 100 100 \n'
               '2020, Fall, ENGL015 100 100 100 100 \n'
               '2020, Fall, KINES101 100 100 100 100 \n'
               '2020, Fall, PSU001 100 100 100 100 \n'
               '2020, Fall, COMM100 100 100 100 100 \n'
               ]

student10 = ['abc0010\n',
               '2020, Fall, CMPSC131 100 100 100 100 \n'
               '2020, Fall, MATH140 100 100 100 100 \n'
               '2020, Fall, ENGL015 100 100 100 100 \n'
               '2020, Fall, KINES101 100 100 100 100 \n'
               '2020, Fall, PSU001 100 100 100 100 \n'
               '2020, Fall, COMM100 100 100 100 100 \n'
               ]

student11 = ['abc0011\n',
               '2020, Fall, CMPSC131 100 100 100 100 \n'
               '2020, Fall, MATH140 100 100 100 100 \n'
               '2020, Fall, ENGL015 100 100 100 100 \n'
               '2020, Fall, KINES101 100 100 100 100 \n'
               '2020, Fall, PSU001 100 100 100 100 \n'
               '2020, Fall, COMM100 100 100 100 100 \n'
               ]

student12 = ['abc0012\n',
               '2020, Fall, CMPSC131 100 100 100 100 \n'
               '2020, Fall, MATH140 100 100 100 100 \n'
               '2020, Fall, ENGL015 100 100 100 100 \n'
               '2020, Fall, KINES101 100 100 100 100 \n'
               '2020, Fall, PSU001 100 100 100 100 \n'
               '2020, Fall, COMM100 100 100 100 100 \n'
               ]

student13 = ['abc0013\n',
               '2020, Fall, CMPSC131 100 100 100 100 \n'
               '2020, Fall, MATH140 100 100 100 100 \n'
               '2020, Fall, ENGL015 100 100 100 100 \n'
               '2020, Fall, KINES101 100 100 100 100 \n'
               '2020, Fall, PSU001 100 100 100 100 \n'
               '2020, Fall, COMM100 100 100 100 100 \n'
               ]

student14 = ['abc0014\n',
               '2020, Fall, CMPSC131 100 100 100 100 \n'
               '2020, Fall, MATH140 100 100 100 100 \n'
               '2020, Fall, ENGL015 100 100 100 100 \n'
               '2020, Fall, KINES101 100 100 100 100 \n'
               '2020, Fall, PSU001 100 100 100 100 \n'
               '2020, Fall, COMM100 100 100 100 100 \n'
               ]

student15 = ['abc0015\n',
               '2020, Fall, CMPSC131 100 100 100 100 \n'
               '2020, Fall, MATH140 100 100 100 100 \n'
               '2020, Fall, ENGL015 100 100 100 100 \n'
               '2020, Fall, KINES101 100 100 100 100 \n'
               '2020, Fall, PSU001 100 100 100 100 \n'
               '2020, Fall, COMM100 100 100 100 100 \n'
               ]


def student0_course():       #this is just an example of how the other 15 works
    with open('database.txt','w+') as gradefile:
        read = gradefile.readlines()
        gradefile.write(student0[0])
        gradefile.writelines(student0[1])
        gradefile.close()

def student1_course():
    with open('database.txt','w+') as gradefile:
        read = gradefile.readlines()
        gradefile.write(student1[0])
        gradefile.writelines(student1[1])
        gradefile.close()

def student2_course():
    with open('database.txt','w+') as gradefile:
        read = gradefile.readlines()
        gradefile.write(student2[0])
        gradefile.writelines(student2[1])
        gradefile.close()

def student3_course():
    with open('database.txt','w+') as gradefile:
        read = gradefile.readlines()
        gradefile.write(student3[0])
        gradefile.writelines(student3[1])
        gradefile.close()

def student4_course():
    with open('database.txt','w+') as gradefile:
        read = gradefile.readlines()
        gradefile.write(student4[0])
        gradefile.writelines(student4[1])
        gradefile.close()

def student5_course():
    with open('database.txt','w+') as gradefile:
        read = gradefile.readlines()
        gradefile.write(student5[0])
        gradefile.writelines(student5[1])
        gradefile.close()

def student6_course():
    with open('database.txt','w+') as gradefile:
        read = gradefile.readlines()
        gradefile.write(student6[0])
        gradefile.writelines(student6[1])
        gradefile.close()

def student7_course():
    with open('database.txt','w+') as gradefile:
        read = gradefile.readlines()
        gradefile.write(student7[0])
        gradefile.writelines(student7[1])
        gradefile.close()

def student8_course():
    with open('database.txt','w+') as gradefile:
        read = gradefile.readlines()
        gradefile.write(student8[0])
        gradefile.writelines(student8[1])
        gradefile.close()

def student9_course():
    with open('database.txt','w+') as gradefile:
        read = gradefile.readlines()
        gradefile.write(student9[0])
        gradefile.writelines(student9[1])
        gradefile.close()

def student9_course():
    with open('database.txt','w+') as gradefile:
        read = gradefile.readlines()
        gradefile.write(student9[0])
        gradefile.writelines(student9[1])
        gradefile.close()

def student10_course():
    with open('database.txt','w+') as gradefile:
        read = gradefile.readlines()
        gradefile.write(student10[0])
        gradefile.writelines(student10[1])
        gradefile.close()

def student11_course():
    with open('database.txt','w+') as gradefile:
        read = gradefile.readlines()
        gradefile.write(student11[0])
        gradefile.writelines(student11[1])
        gradefile.close()

def student12_course():
    with open('database.txt','w+') as gradefile:
        read = gradefile.readlines()
        gradefile.write(student12[0])
        gradefile.writelines(student12[1])
        gradefile.close()

def student13_course():
    with open('database.txt','w+') as gradefile:
        read = gradefile.readlines()
        gradefile.write(student13[0])
        gradefile.writelines(student13[1])
        gradefile.close()

def student14_course():
    with open('database.txt','w+') as gradefile:
        read = gradefile.readlines()
        gradefile.write(student14[0])
        gradefile.writelines(student14[1])
        gradefile.close()

def student15_course():
    with open('database.txt','w+') as gradefile:
        read = gradefile.readlines()
        gradefile.write(student15[0])
        gradefile.writelines(student15[1])
        gradefile.close()


def course():
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

        course()        #to open the notepad file


def change():
    print()

if __name__ == '__main__':
    main()
