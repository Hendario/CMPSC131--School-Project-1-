import csv

def main():

    while True:
        meun()
        choice = int(input('Plese slecte'))
        if choice in [1,2,3,]:
            if choice == 1:
                student_id()
                break

            elif choice == 2:
                course()

            elif choice == 3:
                change()
                break
def meun():
    print("----------------meun--------------------")
    print("|         1.Student information        |")
    print("|         2.Courses                    |")
    print("----------------------------------------")

def student_id():
    with open('students.csv','r') as csvfile:
        reader = csv.DictReader(csvfile)
        student_id = input('Enter the student number: ')
        for row in reader:
            if student_id == row['student_id']:
                for key, value in row.items():
                    print(key, ':', value)
                break

            else:
                print('This number does not exist')

def course():
    with open('courses.csv','r') as gradefile:
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
