#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'slowestKey' function below.
#
# The function is expected to return a CHARACTER.
# The function accepts 2D_INTEGER_ARRAY keyTimes as parameter.
#

def slowestKey(keyTimes):
    keyTimes = [[chr(k[0]+97), k[1]] for k in keyTimes]
    longestKey=None
    longestDuration=None
    for i in range (len(keyTimes)-1):
        if i == 0:
            start = 0
        else:
            start = keyTimes[i-1][1]
        end = keyTimes[i][1]
        char = keyTimes[i][0]
        interval = end - start
        if not longestDuration or interval > longestDuration:
            longestDuration = interval
            longestKey = char
    return longestKey
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    keyTimes_rows = int(input().strip())
    keyTimes_columns = int(input().strip())

    keyTimes = []

    for _ in range(keyTimes_rows):
        keyTimes.append(list(map(int, input().rstrip().split())))

    result = slowestKey(keyTimes)

    fptr.write(str(result) + '\n')

    fptr.close()
