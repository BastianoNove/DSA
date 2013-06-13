def edit_distance(x, y):
    xn = len(x)
    yn = len(y)
    x = ' ' + x
    y = ' ' + y
    dp = [[0 for _ in range(yn+1)] for _ in range(xn+1)]
    dp[0] = [0] + [i for i in range(1, yn+1)]
    for i in range(1,xn+1):
        dp[i][0] = i

    for i in range(1, xn+1):
        for j in range(1,yn+1):
            dp[i][j] = min(dp[i-1][j] + 1,
                           dp[i][j-1] + 1,
                           dp[i-1][j-1] + int(x[i]!=y[j]))
    return dp[xn][yn]

def print_table(table):
    for row in table:
        print(row)

def test():
    assert(edit_distance('good', 'goodbye') == 3)
    assert(edit_distance('kitten', 'sitting') == 3)
    assert(edit_distance('hello', 'hello') == 0)
    assert(edit_distance('free', 'style') == 4)
    print('test pass')

test()
