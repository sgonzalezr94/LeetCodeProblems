# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms


from math import inf


def minimumAbsoluteDifference(arr):
    sorted_array = sorted(arr)
    min_diff = abs(sorted_array[-1] - sorted_array[0])
    for i in range(len(sorted_array) - 1):
        min_diff = min(abs(sorted_array[i] - sorted_array[i + 1]), min_diff)
    return min_diff
