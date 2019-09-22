# -*- coding:utf-8 -*-  
# 最长公共子串
def get_last_result(dp, r, l):
    if l<1 or r<1:
        return 0
    return dp[r][l]

def longest_common_serial(source, target):
    dp = [[] for _ in range source]
    for i, l1 in enumerate(source):
        for j, l2 in enumerate(target):
            if l1==l2:
                dp[l1][l2] = 1 + get_last_result(dp, l1, l2)
            else:
                dp[l1][l2] = 0
    return max([max(x) for x in dp])

# 最长公共子序列
def get_last_helper1(dp, r, l):
    if l<1 and r<1:
        return 0
    if l<1:
        return dp[r-1][l]
    if r<1:
        return dp[r][l-1]
    return max((dp[r-1][l], dp[r][l-1]))

def get_last_helper2(dp, r, l):
    if l<1 or r<1:
        return 0
    return dp[r-1][l-1]

def longest_common_serial2(source, target):
    dp = [[] for _ in range source]
    for i, l1 in enumerate(source):
        for j, l2 in enumerate(target):
            if l1==l2:
                dp[l1][l2] = 1 + get_last_helper2(dp, l1, l2)
            else:
                dp[l1][l2] = get_last_helper1(dp, l1, l2)
    return dp[len(source)-1][len(target)-1]