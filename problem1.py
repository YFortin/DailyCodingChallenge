"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

from time import perf_counter
import random

def answer(numbers, k):
    for first_index, first_number in enumerate(numbers):
        for second_index, second_number in enumerate(numbers):
            if first_index != second_index:  
                if first_number + second_number == k:
                    return True
    return False


#In one pass
def better_answer(numbers, k):
    remainders = set([])
    for number in numbers:
        if number <= k:
            if number in remainders:
                return True
            else:
                remainders.add(k - number)
    return False


if __name__ == "__main__":
    assert(answer([10, 15, 3, 7], 17))
    assert(answer([1, 2, 3], 6) == False)
    assert(answer([1, 2, 1], 2))
    assert(answer([1, 0, 0], 2) == False)

    assert(better_answer([10, 15, 3, 7], 17))
    assert(better_answer([1, 2, 3], 6) == False)
    assert(better_answer([1, 2, 1], 2))
    assert(better_answer([1, 0, 0], 2) == False)

    #performance
    numbers = [random.randint(1,100) for _ in range(5000)]

    start = perf_counter()
    answer(numbers, 0)
    stop = perf_counter()
    print('answer', stop-start, 'seconds')

    start = perf_counter()
    better_answer(numbers, 0)
    stop = perf_counter()
    print('better_answer', stop-start, 'seconds')