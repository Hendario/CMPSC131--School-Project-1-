import csv
import webbrowser

#PART 1
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
                change_Student_inform()

            elif choice == 4:
                change_student_courses()

            elif choice == 5:
                print('❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤')
                print('❤You have exit our menu❤')
                print('❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤')
                break
#This is the MEUN
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
               pass
           if choice == 1:
               student_inform()


           elif choice == 2:
               read_ids()

           elif choice == 3:
               change_Student_inform()
               break
           elif choice == 4:
               change_student_courses()

           elif choice == 5:
               print('❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤')
               print('❤You have exit our menu❤')
               print('❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤')
               break

#---------------------------------------------------------------------------------------------
#this is the system for part 2, and will display the specific student's courses

#I deleted all others, and decide to put it in all different database

def student0_course():       #this is just an example of how the other 15 works
    f = open("database.txt", "r")
    print(f.read())
    f.close()

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


def student1_course_datas():
    with open('database1.txt', 'r') as gradefile:
        print(webbrowser.open("database1.txt"))
        gradefile.close()
def student2_course_datas():
    with open('database2.txt', 'r') as gradefile:
        print(webbrowser.open("database2.txt"))
        gradefile.close()
def student3_course_datas():
    with open('database3.txt', 'r') as gradefile:
        print(webbrowser.open("database3.txt"))
        gradefile.close()
def student4_course_datas():
    with open('database4.txt', 'r') as gradefile:
        print(webbrowser.open("database4.txt"))
        gradefile.close()
def student5_course_datas():
    with open('database5.txt', 'r') as gradefile:
        print(webbrowser.open("database5.txt"))
        gradefile.close()
def student6_course_datas():
    with open('database6.txt', 'r') as gradefile:
        print(webbrowser.open("database6.txt"))
        gradefile.close()
def student7_course_datas():
    with open('database7.txt', 'r') as gradefile:
        print(webbrowser.open("database7.txt"))
        gradefile.close()
def student8_course_datas():
    with open('database8.txt', 'r') as gradefile:
        print(webbrowser.open("database8.txt"))
        gradefile.close()
def student9_course_datas():
    with open('database9.txt', 'r') as gradefile:
        print(webbrowser.open("database9.txt"))
        gradefile.close()
def student10_course_datas():
    with open('database10.txt', 'r') as gradefile:
        print(webbrowser.open("database10.txt"))
        gradefile.close()
def student11_course_datas():
    with open('database11.txt', 'r') as gradefile:
        print(webbrowser.open("database11.txt"))
        gradefile.close()
def student12_course_datas():
    with open('database12.txt', 'r') as gradefile:
        print(webbrowser.open("database12.txt"))
        gradefile.close()
def student13_course_datas():
    with open('database13.txt', 'r') as gradefile:
        print(webbrowser.open("database13.txt"))
        gradefile.close()
def student14_course_datas():
    with open('database14.txt', 'r') as gradefile:
        print(webbrowser.open("database14.txt"))
        gradefile.close()
def student15_course_datas():
    with open('database15.txt', 'r') as gradefile:
        print(webbrowser.open("database15.txt"))
        gradefile.close()

#---------------------------------------------------------------------------------------------
#This is the System in meun for (3)
def student_inform_datas():
    with open('Students.csv', 'r') as gradefile:
        print(webbrowser.open('Students.csv'))
        gradefile.close()

#---------------------------------------------------------------------------------------------
#This is the System in menu for (4)
def read_ids():     #read all the ids, and open them with notepad
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
    student_inform_datas()
    print('○○○○○○○○○○○○○○○○○○○○○○○○○')

def change_student_courses():
    print('○○○○○○○○○○○○○○○○○○○○○○○○○')
    print('You can edit anything by using notepad,')
    print('Format:\nYears,Semaster,Class,Test1,Test2,Test3,Test4\n(IMPORTANT:Remember to save the file!!!)')
    student_id = input('Enter your student id to change your course\n')
    if student_id == 'jkl6150':
        print('Opening the file....\nPlease Wait')
        student1_course_datas()
        ans = input('Are you finished?(Yes?)')
        if ans == 'Yes':
            print('Your change have been saved')
        else:
            print('Your file might not saved')
    elif student_id == 'jmc8444':
        print('Opening the file....\nPlease Wait')
        student2_course_datas()
        ans = input('Are you finished?(Yes?)')
        if ans == 'Yes':
            print('Your change have been saved')
        else:
            print('Your file might not saved')
    elif student_id == 'abc0003':
        print('Opening the file....\nPlease Wait')
        student3_course_datas()
        ans = input('Are you finished?(Yes?)')
        if ans == 'Yes':
            print('Your change have been saved')
        else:
            print('Your file might not saved')
    elif student_id == 'abc0004':
        print('Opening the file....\nPlease Wait')
        student4_course_datas()
        ans = input('Are you finished?(Yes?)')
        if ans == 'Yes':
            print('Your change have been saved')
        else:
            print('Your file might not saved')
    elif student_id == 'abc0005':
        print('Opening the file....\nPlease Wait')
        student5_course_datas()
        ans = input('Are you finished?(Yes?)')
        if ans == 'Yes':
            print('Your change have been saved')
        else:
            print('Your file might not saved')
    elif student_id == 'abc0006':
        print('Opening the file....\nPlease Wait')
        student6_course_datas()
        ans = input('Are you finished?(Yes?)')
        if ans == 'Yes':
            print('Your change have been saved')
        else:
            print('Your file might not saved')
    elif student_id == 'abc0007':
        print('Opening the file....\nPlease Wait')
        student7_course_datas()
        ans = input('Are you finished?(Yes?)')
        if ans == 'Yes':
            print('Your change have been saved')
        else:
            print('Your file might not saved')
    elif student_id == 'abc0008':
        print('Opening the file....\nPlease Wait')
        student8_course_datas()
        ans = input('Are you finished?(Yes?)')
        if ans == 'Yes':
            print('Your change have been saved')
        else:
            print('Your file might not saved')
    elif student_id == 'abc0009':
        print('Opening the file....\nPlease Wait')
        student9_course_datas()
        ans = input('Are you finished?(Yes?)')
        if ans == 'Yes':
            print('Your change have been saved')
        else:
            print('Your file might not saved')
    elif student_id == 'abc0010':
        print('Opening the file....\nPlease Wait')
        student10_course_datas()
        ans = input('Are you finished?(Yes?)')
        if ans == 'Yes':
            print('Your change have been saved')
        else:
            print('Your file might not saved')
    elif student_id == 'abc0011':
        print('Opening the file....\nPlease Wait')
        student11_course_datas()
        ans = input('Are you finished?(Yes?)')
        if ans == 'Yes':
            print('Your change have been saved')
        else:
            print('Your file might not saved')
    elif student_id == 'abc0012':
        print('Opening the file....\nPlease Wait')
        student12_course_datas()
        ans = input('Are you finished?(Yes?)')
        if ans == 'Yes':
            print('Your change have been saved')
        else:
            print('Your file might not saved')
    elif student_id == 'abc0013':
        print('Opening the file....\nPlease Wait')
        student13_course_datas()
        ans = input('Are you finished?(Yes?)')
        if ans == 'Yes':
            print('Your change have been saved')
        else:
            print('Your file might not saved')
    elif student_id == 'abc0014':
        print('Opening the file....\nPlease Wait')
        student14_course_datas()
        ans = input('Are you finished?(Yes?)')
        if ans == 'Yes':
            print('Your change have been saved')
        else:
            print('Your file might not saved')
    elif student_id == 'abc0015':
        print('Opening the file....\nPlease Wait')
        student15_course_datas()
        ans = input('Are you finished?(Yes?)')
        if ans == 'Yes':
            print('Your change have been saved')
        else:
            print('Your file might not saved')
    else:
        print('This student id does not exist')

    print('○○○○○○○○○○○○○○○○○○○○○○○○○')

Students_ = {'jkl6150': 'Freshmen',     #01
             'jmc8444': 'Freshmen',     #02
             'abc0003': 'Sophomore',    #03
             'abc0004': 'Junior',       #04
             'abc0005': 'Senior',       #05
             'abc0006': 'Junior',       #06
             'abc0007': 'Senior',       #07
             'abc0008': 'Sophomore',    #08
             'abc0009': 'Senior',       #09
             'abc0010': 'Senior',       #10
             'abc0011': 'Senior',       #11
             'abc0012': 'Freshmen',     #12
             'abc0013': 'Senior',       #13
             'abc0014': 'Freshmen',     #14
             'abc0015': 'Senior'        #15
             }

if __name__ == '__main__':
    main()
