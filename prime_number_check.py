'''checking the number is prime or not'''

import math
def prime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    i = 2
    while i <= math.sqrt(number):
        if number % i == 0:
            return False
        i += 1
    return True
number = int(input())
bool = prime(number)
print("prime"if bool == True else "not prime")
