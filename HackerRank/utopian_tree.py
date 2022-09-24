# https://www.hackerrank.com/challenges/utopian-tree/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# Period  Height
# 0          1
# 1          2
# 2          3
# 3          6
# 4          7
# 5          14

result_dict = {0: 1}


def utopianTree(n):
    if n in result_dict:
        return result_dict[n]
    else:
        if n % 2 != 0:
            if n - 1 in result_dict:
                response = 2 * result_dict[n - 1]
            else:
                response = 2 * utopianTree(n - 1)

            result_dict[n] = response
            return response
        if n % 2 == 0:
            if n - 1 in result_dict:
                response = result_dict[n - 1] + 1
            else:
                response = utopianTree(n - 1) + 1
            result_dict[n] = response
            return response
