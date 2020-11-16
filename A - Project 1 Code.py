import csv
import webbrowser
#The full description will be in our WALKTHROUGH / Which is in Github, WE KNOW THIS IS KINDA MESS. I MEAN REALLY MESS

#PART 1
def main():

    while True:
        meun()
        choice = int(input('Plese select\n'))
        if choice in [1,2,3,4,5,6,7]:
            if choice == 1:
                student_inform()

            elif choice == 2:
                read_ids()

            elif choice == 3:
                change_Student_inform()

            elif choice == 4:
                change_student_courses()

            elif choice == 5:
                student_academic_standing()

            elif choice == 6:
                add()

            elif choice == 7:
                print('❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤')  #This is just some customizize form, just for look better
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
    print("|         5.Check Class Standing       |")
    print("|         6.Add student inform         |")
    print("|         7.Exit                       |")
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
    print('Opening file')
    print('......')
    student_inform_datas()
    ask = input('Did you saved your csv file?(Yes?)\n')
    if ask == 'Yes':
        print('Good.')
    else:
        print('You may not save you data')
    print('○○○○○○○○○○○○○○○○○○○○○○○○○')

def change_student_courses():
    print('○○○○○○○○○○○○○○○○○○○○○○○○○')
    print('You can edit anything by using notepad,')
    print('Format:\nYears,Semaster,Average_assignment,Average_quizzes,Average_projects,Average_exams\n(IMPORTANT:Remember to save the file!!!)')
    student_id = input('Enter your student id to change your course\n')
    if student_id == 'jkl6150':
        print('Opening the file....\nPlease Wait')
        student1_course_datas()
        ans = input('Are you finished?(Yes?)\n')
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

def total_courses():
    databases = ['databse1.txt','databse2.txt']
    students_file = open(databases[0],'r')
    print(students_file)

#A dict of student's academic standing
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

def student_academic_standing():
    print('○○○○○○○○○○○○○○○○○○○○○○○○○')
    id_found = str(input('Enter your student id to see your academic standing\n'))
    for student_id in Students_:
        if student_id == id_found:
            student_grade = Students_[student_id]
            print('Student grade for {}, \nis: {}'.format(id_found,student_grade))
            break
    else:
        print('Student id not found')

    print('○○○○○○○○○○○○○○○○○○○○○○○○○')

filename = 'students.txt'

def add():
    stdentList = []  # Save a list of student information
    mark = True
    while mark:
        id = input("Plese Enter a Student ID You Want To ADD：")
        if not id:  # when ID is empty, out of the loop
            break
        first_name = input("Please Enter Your First Name：")
        if not first_name:  # when name is empty, out of the loop
            break
        last_name = input('Please Enter Your Last name:')
        if not last_name:
            break
        try:
            phone_num = int(input("Please Enter Your Phone Number："))
            email = input("Please Enter Your Email ID：")
            major = input("Please Enter Your Major：")
        except:
            print("This is invalid. . . . Re-enter information")
            continue
        stdent = {"Stuent ID": id, "First name": first_name,"Last name": last_name, "Phone number": phone_num, "Email ID": email, "Major": major}  # 将输入的学生信息保存到字典
        stdentList.append(stdent)  # Add student dictionary to list
        inputMark = input("DO You Want To Keep Adding Information?（Yes or No）:")
        if inputMark == "Yes":  # Keep adding
            mark = True
        else:  # Do not continue to add
            mark = False
    save(stdentList)  # Save student information to file
    print("The Student Information is Entered! ! !")


# Save student information to file
def save(student):
    try:
        students_txt = open(filename, "a")  # Open in append mode
    except Exception as e:
        students_txt = open(filename, "w+")  # when the file does not exist,it will create a file and open
    for info in student:
        students_txt.write(str(info) + "\n")  # Store by line, add line break
    students_txt.close()  # close the file


if __name__ == '__main__':
    main()
