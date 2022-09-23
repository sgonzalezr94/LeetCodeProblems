# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem?isFullScreen=true


def catAndMouse(x, y, z):
    cat_a = abs(x - z)
    cat_b = abs(y - z)
    if cat_a == cat_b:
        return "Mouse C"
    if cat_a < cat_b:
        return "Cat A"
    else:
        return "Cat B"
