def gradingStudents(grades):
    final = []
    for grad in grades:
        num = grad % 5
        if grad < 38:
            final.append(grad)
        elif (round(grad/5)*5 - grad) < 3 and (round(grad/5)*5 - grad) > 0:
            final.append(round(grad/5)*5)
        else:
            final.append(grad)

    return final
