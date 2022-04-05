from work3 import circle_opt,invalid as inv
from test import hello as h

def sum(a,b):
    return a+b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b

def diff(a,b):
    return a-b

def odd(a):
    return a%2


print('This program is for arithmetic computation')

print('1.Addition\t\t\t2.Subtraction\n3.Multiplication\t4.Division\n5.Odd Number\t\t6.Even Number\n7.CGPA')
opt = int(input('Çhoose your option (1~6): '))

if opt == 1 or opt == 2 or opt == 3 or opt == 4:

    a = float(input('Enter the First Number: '))
    b = float(input('Enter the Second Number: '))

    if opt == 1:
        print('Sum = ' + str(sum(a,b)))
    elif opt == 2:
        print('Difference = ' + str(diff(a,b)))
    elif opt == 3:
        print('Multiplication = ' + str(mult(a,b)))
    else:
        print('Division = ' + str(div(a,b)))

elif opt == 5 or opt == 6:
    a = int(input('Enter the Number: '))
    if odd(a) == 1:
        print(str(a) + ' is an Odd Number!!!')
    else:
        print(str(a) + ' is an Even Number!!!')
elif opt == 7:
    circle_opt()
elif opt == 8:
    from work import *

elif opt == 9:
    print(h.a)
else:
    inv()