#!/bin/python3

import random

map = [
    [[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False]],
    [[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False]],
    [[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False]],
    [[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False]],
    [[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False]],
    [[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False]],
    [[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False]],
    [[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False]],
    [[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False],[" ",False]]
]

def generate():
    for 10 in range:

        randpos1 = random.randint(0,9)
        randpos2 = random.randint(0,9)
        str(randnum) = random.randint(0,9)

        if map[randpos1][randpos2][1] != True:
            map[randpos1][randpos2][1] = True
            map[randpos1][randpos2][0] = randnum

        else:
            while map[randpos1][randpos2][1] == True:
                randpos1 = random.randint(0,9)
                randpos2 = random.randint(0,9)

            map[randpos1][randpos2][1] = True
            map[randpos1][randpos2][0] = randnum

        print(map[randpos1][randpos2])


def mark():
    zahlen = ["1","2","3","4","5","6","7","8","9"]

    pos1 = input("pos1: ")

    if pos1 in zahlen:
        pos1 = int(pos1)
        pos1 -= 1

        pos2 = input("pos2: ")

        if pos2 in zahlen:
            pos2 = int(pos2)
            pos2 -= 1
            if map[pos1][pos2][1] == False:
                new_num = input("new entry")

                if new_num in zahlen:
                    map[pos1][pos2][0] = new_num
                else:
                    print("error")
            else:
                print("already occupied")
        else:
            print("error")
    else:
        print("error")

#mark()

#print(map1)
#print(map2)

#print(map1[0][0])
#print("pos1: ", pos1, "pos2: ", pos2, "map2[0][0]:\n", map2[0][0])