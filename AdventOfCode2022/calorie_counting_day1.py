class Solution:
    def __init__(self, day: int) -> None:
        self.day = day
        self.elves_calories = list()

    def get_maximum_calories(self, day: int) -> int:
        with open(
            f"inputs/{day}.txt", "r"
        ) as input:  # didn't create a _read_input function since while iterating and splitting the data we could start grouping and adding on the same loop.
            max_calories = 0
            carried_calories = 0
            for line in input.readlines():
                line = line.strip()
                if line:
                    current_calories = int(line)
                    carried_calories += current_calories
                else:
                    self.elves_calories.append(carried_calories)
                    if max_calories <= carried_calories:
                        max_calories = carried_calories
                    carried_calories = 0
        return max_calories

    def top_three_elves(self):
        """This must be executed after calculating the list of calories/elve for the set of elves,if not the list will be empty."""
        self.elves_calories.sort(reverse=True)
        return sum(self.elves_calories[0:3])


sol = Solution(1)
a = sol.get_maximum_calories(sol.day)
b = sol.top_three_elves()
