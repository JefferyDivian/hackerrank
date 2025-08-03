def PlusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    for i in arr: #iteration through the array
        if i>0:
            pos+=1  #counting pos if the no is greater than 0
        elif i<0:
            neg+=1 #counting negative if the no is lesser than 0
        else:
            zero+=1  #counting pos if the no is lesser than 0
    return (pos,neg,zero)