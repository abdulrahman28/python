from ex3 import *
if mno == 'admin' and pword == 'admin':
    a = input('Enter the Matric no.: ')
    from ex4 import *
    b = check_file(a,'db')
    if b == False:
        f = open('db', 'a')
        f.write(a+',')
        print(a+', has been added successfully!!!')
        f.close()
