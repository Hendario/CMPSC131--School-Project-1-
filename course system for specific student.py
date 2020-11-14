

student1 = ['jkl6150\n',
               '2015, spring, CS123 90 91 98 92 \n'
               '2015, spring, CS120 80 70 75 2 \n'
               '2015, spring, Math250 92 84 88 91 \n'
               '2016, spring, CS131 90 91 98 92 \n'
               '2016, spring, CS125 80 70 75 2 \n'
               '2016, fall Math252 92 84 88 91 \n'
               ]


def student1_course():
    with open('Student1_courses.txt','w+') as gradefile:
        read = gradefile.readlines()
        gradefile.write(student1[0])
        gradefile.writelines(student1[1])
        gradefile.close()

student1_course()