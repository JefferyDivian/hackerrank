def compareTriplets(a,b):
    alice,bob=0,0
    for i in zip(a,b):
        if i[0]>i[1]:
            alice+=1
        elif i[1]>i[0]:
            bob+=1
    return (alice,bob)


