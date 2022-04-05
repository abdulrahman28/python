
def invalid():
    print('Invalid Option, Pls try again!!!')

def circle(a,r):
    pi = 3.142
    if a == 'area' or a == '1' or a == 'a':
        return pi * r * r
    elif a == 'circumference' or a == '2' or a == 'c':
        return 2 * pi * r

def circle_opt():
    print('Circle Geometry Selected!!!\n1. Area\t\t2. Circumference')
    a = input('Choose your option: ')
    a = a.lower()
    r = float(input('Enter the radius of the Circle: '))
    ans = 'The {} of the Circle with radius {}cm = {}{}'
    if a == '1' or a == 'a' or a == 'area':
        print(ans.format('Area',r,circle(a,r),'cm^2'))
    elif a == '2' or a == 'c' or a == 'circumference':
        print(ans.format('Circumference',r,circle(a,r),'cm'))
    else:
        invalid()

i = 1
while i == 1:
    print('\nProgram to compute Geometry')
    print('1. Circle\t2. Square\t3. Rectangle\t4. Triangle')
    a = input('Enter your option: ')
    a = a.lower()
    if a == '1' or a == 'c' or a == 'circle':
        circle_opt()
    else:
        invalid()

    a = input('\nDo you want to run program again (Y/N): ')
    a = a.upper()
    if a == 'Y' or a == 'YES':
        i = 1
    else:
        i = 0
