def birthday(s,d,m):
    out = 0
    leng = len(s)
    for i in range(0,leng):
        if sum(s[i : i+m]) == d:
            out += 1
    return(out)