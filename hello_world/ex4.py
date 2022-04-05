def check_file(a,b):
    f = open(b,'r')
    b = f.readlines()
    b = b[0].split(',')
    for x in b:
        if a == x:
            f.close()
            return True
    return False