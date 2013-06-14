#!/usr/bin/env python

def knapsack(w, c):
    w = [0] + w
    dp = [[0 for _ in xrange(c+1)] for _ in xrange(len(w))]
    dp[0][0] = 1
    print_table(dp)
    for i in range(1, len(w)):
        for j in range(1, c+1):
            if (w[i] > j):
                dp[i][j] = 0 
            else:
                print(j-w[i])
                dp[i][j] = int(dp[i-1][j-w[i]] == 1)
    print_table(dp)
    return dp[len(w)-1][c]


def print_table(dp):
    for row in dp:
        print row
    print

def test():
    print knapsack([1,2,3], 5)

test()

