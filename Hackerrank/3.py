#!/bin/python3

import math
import os
import random
import re
import sys

#['7', '3']
#

#first_multiple_input = input().rstrip().split()
first_multiple_input = ['7', '3']
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

# for _ in range(n):
#     matrix_item = input()
#     matrix.append(matrix_item)

matrix = ['Tsi', 'h%x', 'i #', 'sM ', '$a ', '#t%', 'ir!']
decoded = ""
for i in range(m):
    for letras in matrix:decoded += letras[i]
    
print(re.sub(r'\b[^a-zA-Z0-9]+\b', r' ', decoded))