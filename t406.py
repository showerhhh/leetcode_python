class Solution:
    def reconstructQueue(self, people: list) -> list:
        if not people:
            return []

        def func(x):
            return -x[0], x[1]

        people.sort(key=func)
        new_people = [people[0]]
        for i in people[1:]:
            new_people.insert(i[1], i)
        return new_people
