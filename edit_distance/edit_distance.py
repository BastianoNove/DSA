#!/usr/bin/env python

def edit_distance(x, y):
    x = ' ' + x
    y = ' ' + y
    dp = [[0 for _ in range(len(y))] for _ in range(len(x))]
    dp[0] = [0] + [i for i in range(1, len(y))]
    for i in range(1, len(x)):
        dp[i][0] = i

    for i in range(1, len(x)):
        for j in range(1,len(y)):
            dp[i][j] = min(dp[i-1][j] + 1,
                           dp[i][j-1] + 1,
                           dp[i-1][j-1] + int(x[i]!=y[j]))
    return dp[len(x)-1][len(y)-1]

def print_table(table):
    for row in table:
        print(row)

def test():
    assert(edit_distance('good', 'goodbye') == 3)
    assert(edit_distance('kitten', 'sitting') == 3)
    assert(edit_distance('hello', 'hello') == 0)
    assert(edit_distance('free', 'style') == 4)
    print('test pass')

if __name__ == '__main__':
    test()
