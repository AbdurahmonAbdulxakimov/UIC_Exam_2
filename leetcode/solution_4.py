class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        earliest_year: int = logs[0][0]
        last_year: int = logs[0][0]

        for birth, death in logs:
            if birth < earliest_year:
                earliest_year = birth

            if death > last_year:
                last_year = death

        pop: list = [0] * (last_year - earliest_year + 1)

        for birth, death in logs:
            pop[birth - earliest_year] += 1
            pop[death - earliest_year] -= 1

        max_pop = 0
        year = 0
        current_pop = 0

        for i in range(earliest_year, last_year):
            current_pop += pop[i - earliest_year]
            if current_pop > max_pop:
                max_pop = current_pop
                year = i

        return year
