# https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting&h_r=next-challenge&h_v=zen

# All players look like [Name,Score]
from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"{self.name} {self.score}"

    def comparator(a, b):
        if a.score == b.score:
            if a.name < b.name:
                return -1
            return 0
        if a.score > b.score:
            return -1
        else:
            return 1


data = []
for i in range(3):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, key=cmp_to_key(Player.comparator))
print(data)
