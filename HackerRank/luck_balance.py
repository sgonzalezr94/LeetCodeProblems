# https://www.hackerrank.com/challenges/luck-balance/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms&h_r=next-challenge&h_v=zen


def luckBalance(k, contests):
    contest_dict = dict()
    for contest in contests:
        if contest[1] not in contest_dict:
            contest_dict[contest[1]] = [contest[0]]
        else:
            contest_dict[contest[1]].append(contest[0])
    for key in contest_dict:
        contest_dict[key].sort()
    important_luck = 0
    for i in range(k):
        important_luck += contest_dict[1].pop()
    if 0 in contest_dict:
        return important_luck + sum(contest_dict[0]) - sum(contest_dict[1])
    else:
        return important_luck - sum(contest_dict[1])


a = luckBalance(3, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]])
print(a)
