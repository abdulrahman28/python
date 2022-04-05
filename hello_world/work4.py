def sgpa(a,j):
    o = '\nComputing for {} Semester for the {} Level!!!'
    if a == 1:
        print(o.format('First',j))

    elif a == 2:
        print(o.format('Second',j))

    d = 0
    e = 0

    subj = int(input('Enter the number of Course(s): '))

    i = 1
    while i <= subj:
        f = input('Enter the Course Title:')
        a = int(input('Enter the score for ' + f + ': '))
        b = int(input('Enter the credit unit for ' + f + ': '))
        if a > 100:
            c = b * 0
        elif a >= 70:
            c = b * 5
        elif a >= 60:
            c = b * 4
        elif a >= 50:
            c = b * 3
        elif a >= 45:
            c = b * 2
        elif a >= 40:
            c = b * 1
        else:
            c = b * 0
        i += 1

        d += c
        e += b

    return d / e

def gpa_status(mno,gpa):
    print(mno+', Your GPA = ' + str(gpa))
    if gpa >= 4.5:
        print(mno + ', you are in First Class Honours!!!')
    elif gpa >= 3.5:
        print(mno + ', you are in Second Class Honours (Upper Division)!!!')
    elif gpa >= 2.5:
        print(mno + ', you are in Second Class Honours (Lower Division)!!!')
    elif gpa >= 1.5:
        print(mno + ', you are in Third Class Honours!!!')
    else:
         print(mno + ', you are in Probation!!!')

