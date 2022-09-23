# https://www.hackerrank.com/challenges/electronics-shop/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    sums_list = [sum((i, j)) for i in keyboards for j in drives if i + j <= b]
    if sums_list:
        return max(sums_list)
    return -1
