#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'prison' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER_ARRAY h
#  4. INTEGER_ARRAY v
#

def prison(n, m, h, v):
    # Write your code here
    lrgst_h_gp = 1
    lrgst_v_gp = 1
    
    v_cell = [1] * m
    h_cell = [1] * n
    
    if len(h) == 0 and len(v) == 0:
      return lrgst_h_gp * lrgst_v_gp
    
    for vi in v:
      v_cell[vi-1] = 0
    for hi in h:
      h_cell[hi-1] = 0
      
    t_gap = 1
    for i in range(len(v_cell)):
      if v_cell[i] == 1:
        t_gap = 1
      if v_cell[i] == 0:
        t_gap = t_gap + 1
        if t_gap > lrgst_v_gp:
          lrgst_v_gp = t_gap
    
    t_gap = 1
    for i in range(len(h_cell)):
      if h_cell[i] == 1:
        t_gap = 1
      if h_cell[i] == 0:
        t_gap = t_gap + 1
        if t_gap > lrgst_h_gp:
          lrgst_h_gp = t_gap
          
    return lrgst_h_gp * lrgst_v_gp

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    h_count = int(input().strip())

    h = []

    for _ in range(h_count):
        h_item = int(input().strip())
        h.append(h_item)

    v_count = int(input().strip())

    v = []

    for _ in range(v_count):
        v_item = int(input().strip())
        v.append(v_item)

    result = prison(n, m, h, v)

    fptr.write(str(result) + '\n')

    fptr.close()
