from ex2 import *
print('Welcome, Admin\n1. Add Student\t2. Remove Student\t3. Change Student Level')
print('4. Reset Student Password\t5. View Student Profile\t6. Settings')
a = soption()
if a == '1':
    print('Add Student Selected!!!')
    mno = input('Enter the Student Matriculation Number: ')
    if matric_check(mno) == True:
        lvl = input('Enter the Student Level: ')
        #add_matric_up(mno, lvl, 'master_db', 1)
        add_matric_up(mno, lvl, 'master_db1', 2)
    else:
        invalid_matric(mno)
elif a == '2':
    print('Remove Student Selected!!!')
    mno = input('Enter the Student Matriculation Number: ')
    remove_db(mno,'master_db',1)
    remove_db(mno,'master_db1',2)