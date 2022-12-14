class Solution:
    def __init__(self, day_number: int) -> None:
        self.day_number: int = day_number
        self.communication_string: str = ""

    def read_input(self):
        with open(f"inputs/{self.day_number}.txt", "r") as input:
            self.communication_string = input.readline()

    def verify_unique_chars(self, sequence: str) -> bool:
        return len(set(sequence)) == len(sequence)

    def validate_sequences_1(self) -> int:
        initial_index = 0
        final_index = 4
        while True:
            if not self.verify_unique_chars(
                self.communication_string[initial_index:final_index]
            ):
                initial_index += 1
                final_index += 1
            else:
                break
        return final_index, self.communication_string[initial_index:final_index]

    def validate_sequences_2(self) -> int:
        initial_index = 0
        final_index = 14
        while True:
            if not self.verify_unique_chars(
                self.communication_string[initial_index:final_index]
            ):
                initial_index += 1
                final_index += 1
            else:
                break
        return final_index, self.communication_string[initial_index:final_index]


sol = Solution(6)
sol.read_input()
idx, word = sol.validate_sequences_1()  # 1300
idx, word = sol.validate_sequences_2()  # 3986
