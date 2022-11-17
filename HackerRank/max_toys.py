# https://www.hackerrank.com/challenges/mark-and-toys/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting


def maximumToys(prices, k):
    # Write your code here
    prices.sort()
    toys = 0
    for toy_price in prices:
        if k - toy_price >= 0:
            toys += 1
            k = k - toy_price
    return toys


maximumToys([1, 12, 5, 111, 200, 1000, 10], 50)
