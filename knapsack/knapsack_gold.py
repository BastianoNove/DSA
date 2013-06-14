#!/usr/bin/env python

def knapsack(w, c):
    w.sort()
    w = [0] + w
    dp = [[0 for _ in xrange(c+1)] for _ in xrange(len(w))]
    dp[0][0] = 1
    for i in range(1, len(w)):
        for j in range(1, c+1):
            if (w[i] > j):
                dp[i][j] = 0
            else:
                dp[i][j] = int(dp[i-1][j-w[i]] == 1 or (j-w[i] == 0))
    return max(dp[i][c] for i in range(1,len(w)))

def backtrack(dp, c, w):
    output = []
    k = len(w)
    while c:
        for i in range(k-1, 1, -1):
            if dp[i][c]:
                output[0:0] = [i]
                c = c - w[i]
                break
        c = 0 #not possible
    return output

def print_table(dp):
    for row in dp:
        print row
    print

def test():
    assert(knapsack([3,2,1], 7) == 0)
    assert(knapsack([3,2,1], 5) == 1)
    assert(knapsack([1,11,2,89], 13) == 1)
    print 'test pass'

test()

