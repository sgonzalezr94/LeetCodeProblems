# https://www.hackerrank.com/challenges/the-hurdle-race/problem?isFullScreen=true&h_r=next-challenge&h_v=zen


def hurdleRace(k, height):
    max_heigh = max(height)
    return max_heigh - k if max_heigh - k > 0 else 0
