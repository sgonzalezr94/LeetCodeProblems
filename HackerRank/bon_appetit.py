# https://www.hackerrank.com/challenges/bon-appetit/problem?isFullScreen=true


def bonAppetit(bill, k, b):
    # Write your code here
    if k:
        bill.pop(k)
    split_bill_total = sum(bill) // 2
    if b > split_bill_total:
        print(b - split_bill_total)
    if b - split_bill_total == 0:
        print("Bon Appetit")


bonAppetit([3, 10, 2, 9], 1, 7)
