#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    a.sort()
    b.sort()
    if a[-1] > b[0]:
        return 0
    count = 0
    
    for i in range(a[-1], b[0]+1):
        f = [1, 1]
        for j in a:
            if i % j != 0:
                f[0] = 0
                break
        
        for j in b:
            if j % i != 0:
                f[0] = 0
                break

        # print(i, a, b)
        if f[0] and f[1]:
            count += 1
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
