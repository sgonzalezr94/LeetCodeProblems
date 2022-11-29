# https://leetcode.com/problems/insert-delete-getrandom-o1/

# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
import random


class RandomizedSet:
    def __init__(self):
        self.set = set()
        self.elements = list()

    def insert(self, val: int) -> bool:
        if val not in self.set:
            self.set.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.set:
            self.set.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        self.elements = list(self.set)
        random_pick = random.randint(0, len(self.elements) - 1)
        return self.elements[random_pick]


randomizedSet = RandomizedSet()
randomizedSet.insert(1)
## Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2)
## Returns false as 2 does not exist in the set.
randomizedSet.insert(2)
## Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom()
## getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1)
## Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2)
## 2 was already in the set, so return false.
randomizedSet.getRandom()
