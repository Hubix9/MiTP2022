# 1
# 2
# 1
# 4
# 1
# 2
# 1
# 6
# 7


def baby():
    counter = 1
    flag = True
    while not False:
        print("1 - And I was like baby, baby, baby oh")
        if counter == 1:
            print("2 - Like baby, baby, baby no")
            counter += 1
            continue
            print("3 - Baby, baby, baby oh")
            counter += 1
            break
        elif counter == 2 and flag:
            print("4 - I thought you'd always be mine")
            counter -= 1
            flag = False
            continue
            print("5 - Yeah, yeah, yeah")
        print("6 - Now I'm gone")
        break
    print("7 - Gone, gone, gone, I'm gone")
baby()