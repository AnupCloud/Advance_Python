from statistics import mean
from functools import cached_property


class Calculator:
    def __init__(self, values: list[float]):
        self.values = values

    @cached_property
    def calculate_sum(self) -> float:
        print(f'Getting the sum of: {self.values}')
        return sum(self.values)

    def calculate_mean(self) -> float:
        print(f'Getting the mean of: {self.values}')
        return mean(self.values)

    def calculate_sum_and_mean(self) -> tuple[float, float]:
        return self.calculate_sum, self.calculate_mean()


if __name__ == '__main__':
    numbers: list[float] = [5.5, 10.5, 5.5, 35.0, 15.0, 9.0]
    calc: Calculator = Calculator(numbers)
    sum_result, mean_result = calc.calculate_sum_and_mean()

    print("Sum:", sum_result)
    print("Mean:", mean_result)
