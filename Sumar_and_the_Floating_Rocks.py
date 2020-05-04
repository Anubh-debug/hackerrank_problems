#!/bin/python3
#in this solve function is used to find the number of different integral points on a straight line in between two points in which both points are not included.
import math

# Complete the solve function below.
def solve(x1, y1, x2, y2):
    if x1 == x2:
        return abs(y2 - y1) - 1
    elif y2 == y1:
        return abs(x2 - x1) - 1
    else:
        return math.gcd(abs(x2 - x1), abs(y2 - y1)) - 1



if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        x1Y1X2Y2 = input().split()

        x1 = int(x1Y1X2Y2[0])

        y1 = int(x1Y1X2Y2[1])

        x2 = int(x1Y1X2Y2[2])

        y2 = int(x1Y1X2Y2[3])

        result = solve(x1, y1, x2, y2)
        print(result)
