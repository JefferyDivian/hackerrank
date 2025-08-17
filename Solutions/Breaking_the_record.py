def breakingRecords(scores):
    high, low = scores[0], scores[0]
    a, b = 0, 0   # a = high score breaks, b = low score breaks

    for i in scores:
        if i > high:
            a += 1
            high = i
        elif i < low:
            b += 1
            low = i

    return a, b
