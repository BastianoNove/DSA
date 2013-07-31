#!/usr/bin/env python

def knapsack_pocket(w, c, p):
    ''''Given n gold bars of weights w0, w1, w2...wn, can you select exactly
        k bars whose weights add up to exactly p?'''
    w = [0] + w
    # dp[i][k][p]  up to ith bar available, k knapsack capacity, p bars
    dp = [[[0 for _ in range(p+1)] for _ in range(c+1)] for _ in range(len(w))]
    for i in range(len(w)):
        dp[i][0][0] = 1
    for i in range(1, len(w)):
        for j in range(1, c+1):
            for k in range(1, p+1):
                if w[i] > j:
                    dp[i][j][k] = dp[i-1][j][k]
                else:
                    dp[i][j][k] = max(dp[i-1][j-w[i]][k-1], dp[i-1][j][k])
    return max(dp[i][c][p] for i in range(len(w)))

def print_table(dp):
    for item  in dp:
        print(item)
    print

def test():
    assert(knapsack_pocket([1,2,3], 6, 3) == 1)
    assert(knapsack_pocket([5,19,21], 3, 1) == 0)
    assert(knapsack_pocket([1,2,3,4,5,6,7,8,9], 45, 9) == 1)
    print('test pass')

if __name__ == '__main__':
    test()
