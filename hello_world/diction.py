from ex2 import *

mno = '15/30gr002'
db = 'master_db'


def remove_db(mno,db,z):
    try:
        f = open(db, 'r')
        a = f.readlines()
        f.close()
        a = a[0].split(';')
        a.remove('')
        if z == 1:
            a.remove(mno)
            write_new(list_join(a,';'),db)
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
            write_new(list_join(a,';'),db)
    except:
        invalid()

remove_db(mno,db,1)




