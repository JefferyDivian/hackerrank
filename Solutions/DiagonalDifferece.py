def DiagonalDifference(arr):
    leng = len(arr) #capturing the length to iterate through rows
    diag1 = 0 #Capturing diagonal 1 sum
    diag2 = 0 #Capturing diagonal 2 sum
    for i in range(len(arr)):
        diag1 += arr[i][i] #Iterating through the diagonal 1
        diag2 += arr[i][(leng-1)-i] #Iterating through diagonal 2
    return (abs(diag1-diag2)) #Taking absolute for both the diagonals