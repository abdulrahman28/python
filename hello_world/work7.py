from work4 import *
def main_cgpa(mno):
    print('1. Only Semester 2. Only Session 3. Overall Computation')
    a = input('Enter your option: ')
    if a == '1' or a == 'semester':
        gpa = sgpa(0)
        gpa_status(mno,gpa)
    elif a == '2' or a == 'session':
        j = input('Enter the Level to Compute: ')
        tcl = 0
        i = 1
        while i <= 2:
            tcl += sgpa(i,j)
            i+=1

        tcl /= i-1
        t = 'Your CGPA Status for {} Level:'
        print(t.format(j))
        gpa_status(mno,tcl)