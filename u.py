for y in range (15, -16, -1) :
    for x in range (30, -31, -1) :
        if((x/2)**2 + ((5*y/4) -2* (abs(x))**0.5)**2) <=120:
            print("u", end='')
        else:
            print(" ", end='')
    print()