# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


def median(expendidures: list) -> int:
    if len(expendidures) % 2 != 0:
        return expendidures[len(expendidures) // 2]
    return expendidures[len(expendidures) // 2]


def sortedRemove(lst, n):
    # Binary search approach
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if n == lst[mid]:
            lst.pop(mid)
            return lst
        if n > lst[mid]:
            start = mid + 1
        else:
            end = mid - 1


def sortedInsert(lst, n):
    # Binary search approach
    start = 0
    end = len(lst) - 1
    while start < end:
        mid = (start + end) // 2
        if n >= lst[mid]:
            start = mid + 1
        else:
            end = mid - 1
    if n <= lst[start]:
        lst.insert(start, n)
    else:
        lst.insert(start + 1, n)
    return lst


def activityNotifications(expenditure, d):
    notices = 0
    sorted_expenditures = sorted(expenditure[:d])
    to_remove = None
    for idx, exp in enumerate(expenditure[d:]):
        exp_median = median(sorted_expenditures)
        sorted_expenditures = sortedInsert(sorted_expenditures, exp)
        to_remove = expenditure[idx]
        if exp >= 2 * exp_median:
            notices += 1
        sorted_expenditures = sortedRemove(sorted_expenditures, to_remove)
    return notices


EXP = [2, 3, 4, 2, 3, 6, 8, 4, 5]
# EXP = [10, 20, 30, 40, 50]

# EXP = [1, 2, 3, 4, 4]


s = activityNotifications(expenditure=EXP, d=3)
print(s)
