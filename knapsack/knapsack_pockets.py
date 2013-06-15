#!/usr/bin/env python

def knapsack_pocket(w, v, c, p):
    ''''Given n gold bars of weights w0, w1, w2...wn, can you select exactly
        k bars whose weights add up to exactly p?'''
    w = [0] + w
    # dp[i][k][p]  i = ith bar, k knapsack capacity, p bars
    dp = [[[0 for _ in xrange(p+1)] for _ in xrange(c+1)] for _ in xrange(len(w))]
    for i in range(1, len(w)):
        for j in range(1, c+1):
            if (w[i] > j):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])
    return dp[len(w)-1][c]


def print_table(dp):
    for item  in dp:
        for row in item:
            print row
    print

def test():
    pass
test()
