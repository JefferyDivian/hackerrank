def minmaxsum(arr):
    arr.sort() #sorting so get the numbers aligned to add and get the max and min
    mini = sum(arr[0:4]) #adding the first 4
    maxi = sum(arr[1:5]) #adding the last 4
    return mini,maxi