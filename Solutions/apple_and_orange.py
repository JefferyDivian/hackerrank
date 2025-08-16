def countapplesandoranges(s,t,a,b,apples,oranges):
    apple_count = 0
    orange_count = 0

    for app in apples:
        app_loc = a + app
        if app_loc >= s and app_loc<=t:
            apple_count += 1
    for org in oranges:
        org_loc = b + org
        if  org_loc >= s and org_loc<=t:
            orange_count += 1

    return (apple_count,orange_count)