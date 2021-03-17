""" Some nice libraries """
import json
import sys
from random import choice, randint

with open("de_schlachter.json", encoding="utf-8-sig") as raw:
    bible = json.load(raw)

chap = choice(bible)["chapters"]

# Determine the Input
book = sys.argv[1]
chapters = []
if len(sys.argv) == 3:
    chapters = sys.argv[2].split(":")

# print either Verse, Chapter or Book
# depending on the arguments passed
try:
    if len(sys.argv) == 1:
        for i in chap[randint(0, len(chap)-1)]:
            print(i)
    else:
        F = None
        for verse in bible:
            if verse["name"] == sys.argv[1]:
                F = verse["chapters"]

        if chapters == []:
            for line in F:
                for sub in line:
                    print(sub)

        elif len(chapters) == 2:
            print(F[int(chapters[0]) - 1][int(chapters[1]) - 1])

        elif len(chapters) == 1:
            for line in F[int(chapters[0]) - 1]:
                print(line)
        else:
            # raise an error if to many arguments are given
            raise IndexError


except IndexError:
    print("Schreib John 1:20 oder John 1 oder John.")