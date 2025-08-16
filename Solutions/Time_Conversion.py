def timeConversion(s):
    rev_time = s.split(":")
    if rev_time[2][-2:] == 'PM' and rev_time[0] != '12':
        rev_time[0] = str(int(rev_time[0]) + 12)
        rev_time[2] = rev_time[2][:-2]

    elif rev_time[2][-2:] == 'AM' and rev_time[0] == '12':
        rev_time[0] = '00'
        rev_time[2] = rev_time[2][:-2]

    else:
        rev_time[2] = rev_time[2][:-2]

    time = ":".join(rev_time)
    return time


