def Kangaroo(x1,v1,x2,v2):
    max_iteration = abs((x1+v1) - (x2+v2)) + 2
    for i in range(1,max_iteration):
        if x1+(v1*i) == x2+(v2*i):
            return 'YES'
    else :
        return "NO"
