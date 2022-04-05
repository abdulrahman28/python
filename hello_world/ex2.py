def create_prof():
    name = input('Enter your name: ')
    mno = input('Enter your Matric no.: ')
    email = input('Enter your email: ')
    dob = input('Enter your Date of Birth: ')
    pword = input('Enter your password: ')
    c = '3/12/2022'
    age = str(int(c.split('/')[2]) - int(dob.split('/')[2]))
    res = (name, mno, email, dob, pword, age)
    return res

def login():
    uname = input('Enter your Username: ')
    pword = input('Enter your Password: ')
    res = (uname, pword)
    return res

def soption():
    a = input('Select option: ')
    return a

def matric_check(mno):
    if len(mno) == 10 and mno[2] == '/':
        try:
            a = int(mno[0:2])
            a = int(mno[3:5])
            a = int(mno[7:10])
            return True

        except ValueError:
            invalid_matric(mno)
            return False
    else:
        invalid_matric(mno)
        return False

def invalid():
    print('Invalid, Login Details!!!')

def invalid_matric(mno):
    print(mno + ', Invalid Matric Number Entered!!!')

def write_matric(mno,lvl):
    try:
        f = open('master_db', 'a')
        f.write(mno + ';')
        f.close()
        f = open('master_db1', 'a')
        f.write(mno + ',' + lvl + ';')
        f.close()
        print(mno + ', added to the Database!!!')
    except:
        print('Error has occurred!!!')

def add_matric(mno,lvl):
    if matric_check(mno) == True:
        try:
            f = open('master_db', 'r')
            a = f.readlines()
            a = a[0].split(';')
            j = False
            for x in a:
                if mno == x:
                    print(mno + ', already in the Database!!!')
                    j = True
                    break

            if j == False:
                write_matric(mno,lvl)

        except:
            write_matric(mno,lvl)

def del_matric(mno):
    if matric_check(mno) == True:
        f = open('master_db', 'r')
        a = f.readlines()
        f.close()
        a = a[0].split(';')
        try:
            a.remove(mno)
            b = list_join(a,';')
            '''
            b = ''
            i = 0
            while i <= len(a) - 2:
                b += a[i] + ';'
                i += 1
            '''
            f = open('master_db', 'w')
            f.write(b)
            f.close()
            print(mno + ' successfully removed!!!')
        except ValueError:
            print(mno + ' not in the Database!!!')


def check_db(mno,db,z):
    try:
        f = open(db, 'r')
        a = f.readlines()
        f.close()
        a = a[0].split(';')
        a.pop()
        if z == 1:
            if mno in a:
                return True
            else:
                return False
        else:
            for x in a:
                b = x.split(',')
                if mno in b:
                    return True
            return False
    except:
        return False

def list_join(a,c):
    b = ''
    for x in a:
        b += x + c
    return b

def list_join1(a,c):
    b = ''
    i = 0
    while i <= len(a)-2:
        b += a[i] + c
        i += 1
    b += a[i]
    return b

def write_new(a,db):
    try:
        f = open(db, 'w')
        f.write(a)
        f.close()
        op(1)
    except:
        op(0)

def op(a):
    if a == 1:
        print('Operation Successful!!!')
    elif a == 0:
        print('Operation Failed!!!')


def remove_db(mno,db,z):
    if matric_check(mno) == True and check_db(mno,db,z) == True:
        try:
            f = open(db, 'r')
            a = f.readlines()
            f.close()
            a = a[0].split(';')
            a.remove('')
            if z == 1:
                a.remove(mno)
                write_new(list_join(a, ';'), db)
            else:
                i = 0
                j = False
                for x in a:
                    b = x.split(',')
                    if mno in b:
                        a.pop(i)
                        j = True
                    if j == True:
                        break
                    i += 1
                write_new(list_join(a, ';'), db)
        except:
            op(0)
    else:
        op(0)

def add_matric_up(mno,lvl,db,z):
    try:
        if matric_check(mno) == True and check_db(mno,db,z) == False:
            f = open(db, 'a')
            if z == 1:
                f.write(mno + ';')
            else:
                f.write(mno + ',' + lvl + ';')
            f.close()
        else:
            op(0)
    except:
        op(0)

def modify_db(mno,db,alt,p):
    try:
        if matric_check(mno) == True and check_db(mno,db,2) == True:
            f = open(db, 'r')
            a = f.readlines()
            f.close()
            a = a[0].split(';')
            a.pop()
            i = 0
            while i <= len(a) - 1:
                b = a[i].split(',')
                j = False
                if mno in b:
                    b[p] = alt
                    c = list_join1(b, ',')
                    j = True
                if j == True:
                    a[i] = c
                    break
                i += 1
            c = list_join(a, ';')
            write_new(c, db)
    except:
        op(0)
