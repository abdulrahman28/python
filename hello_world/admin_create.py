from ex2 import *
print('\t\tBowen University\n1. Admin Login\t2. Student Login')
if soption() == '1':
    r = login()
    if r[0] == 'admin' and r[1] == 'bowen':
        print('Admin login successful!!!')
        from admin_page import *
    else:
        invalid()


