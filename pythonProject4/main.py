import math


def two_sum(numbers, target):
    result = []
    for n in numbers:
        for num in range(0,len(numbers)):
            if  (n + numbers[num] == target):
                if (n != numbers[num]):
                    result.append(numbers.index(n))
                    result.append(numbers.index(numbers[num]))

    return result[0:2]


two_sum([1234,5678,9012],14690)

print(
two_sum([1234,5678,9012],14690))


