#!/usr/bin/env python

def knapsack(w, v, c):
    w = [0] + w
    v = [0] + v
    dp = [[0 for _ in xrange(c+1)] for _ in xrange(len(w))]
    for i in range(1, len(w)):
        for j in range(1, c+1):
            if (w[i] > j):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])
    return dp[len(w)-1][c]


def print_table(dp):
    for row in dp:
        print row
    print

def test():
    assert(knapsack([1,2,3], [1,2,3], 5) == 5)
    assert(knapsack([1, 5, 3, 4], [15,10, 9, 5], 8) == 29)
    assert(knapsack([12, 2, 1, 4, 1], [4, 2, 1, 10, 2], 15) == 15)
    print 'test pass'

test()
