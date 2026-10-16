class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = customers.count("Y")
        min_penalty = penalty
        best_hour = 0

        for hour, char in enumerate(customers):
            if char == "Y":
                penalty -= 1
            else:
                penalty += 1

            if penalty < min_penalty:
                min_penalty = penalty
                best_hour = hour + 1

        return best_hour