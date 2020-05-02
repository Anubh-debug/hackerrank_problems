#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    divisors_list = []
    i = 1
    max = 0
    while i <= math.sqrt(n):
        if n % i == 0:
            if n / i == i:
                divisors_list.append(i)
            else:
                divisors_list.append(i)
                divisors_list.append(int(n / i))
        i = i + 1
    for j in divisors_list:
        bool = False
        sum = 0
        number = j
        while j > 0:
            sum = sum + int(j % 10)
            j = j / 10
        if sum >= max:
            max = sum 
            bool = True
        if bool == True:
            max2 = number
    print(max2)
        
