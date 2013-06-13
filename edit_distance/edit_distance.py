def edit_distance(x, y):
    dp = [[0 for _ in xrange(len(x)+1)] for _ in xrange(len(y)+1)]
    dp[0] = [0] + [1]*len(x)
    for i in range(1,len(y)+1):
        dp[i][0] = 1
    for item in dp:
        print item

edit_distance('Sebastian', 'ram')
