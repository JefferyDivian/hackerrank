import math
import os
import random
import re
import sys

def simpleArraySum(ar):
    sum = 0
    for i in ar:
        sum+=i
    return sum

if __name__ == 'main':
    fptr = open(os.environ['OUTPATH'],'w')
    ar_count = int(input().strip())
    ar = list(map(int,input().rstrip().split()))
    result = simpleArraySum(ar)
    fptr.write(str(result)+'\n')
    fptr.close()