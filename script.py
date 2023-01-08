import pandas as pd
import time

sv_length = 0

def naming(item):
    path = ("D:/nomadic/teste/"+str(item)+".csv")
    return path

def search_str(filename, word):
    with open(filename, 'r', encoding='latin-1') as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        if word in content:
            print('string exists in a file')
            return 1
        else:
            return 0

word = "nusha-2001"

for x in range(55):
    if x < 1: continue
    if search_str(naming(x),word):
        print(str(x) + " FOUND ")
        break
    else:
        print(" string does not exist in a file called " +naming(x))
        time.sleep(0.1)



