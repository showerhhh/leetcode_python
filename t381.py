import random


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.v = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        flag = val not in self.v
        self.v.append(val)
        return flag

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        flag = val in self.v
        if flag:
            self.v.remove(val)
        return flag

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.v)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
