print('1. Admin\t2. Login')
a = input('Do you want to create account or login (1-2): ')
if a == '1':
    print('Account modification selected!!!')

    a = input('Enter your Matric no.: ')
    from ex4 import *
    a = check_file(a,'db')
    if a == False:
        print('You are not yet a Student!!!')
    elif a == True:
        from ex2 import *
        f = open(mno.replace('/',''),'w')
        wr = name+','+mno+','+pword+','+email+','+dob+','+age
        f.write(wr)
        print(mno+', Your Account has been created Successfully!!!')
        f.close()
elif a == '2':
    print('Login Option Selected!!!')
    uname = input('Enter your Username: ')
    try:
        f = open(uname.replace('/',''),'r')
        pword = input('Enter your Password: ')
        a = f.readlines()
        a = a[0].split(',')
        mno = uname
        if pword == a[2]:
            print(mno+', Your Login has been Successful!!!')
            from work7 import *
            main_cgpa(mno)
        else:
            print(mno+', Invalid login details!!!')
        f.close()
    except:
        print(uname + ' have not yet registered, Pls register before login!!!')