#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'firstRepeatedWord' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def firstRepeatedWord(sentence):
    # Write your code here
    import re
    from collections import Counter
    words = re.split(' |   |,|:|;|-', sentence)
    #sentence.split(' ')
    
    dict = Counter(words)
    
    for key in words:
        if dict[key] > 1:
            print (key)
            return str(key)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = firstRepeatedWord(sentence)

    fptr.write(result + '\n')

    fptr.close()
