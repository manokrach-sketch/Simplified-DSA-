# Backtracking is a general algorithm for finding all (or some) solutions to computational problems,
# notably constraint satisfaction problems, that incrementally builds candidates to the solutions, 
# and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly 
# be completed to a valid solution.

"""
How it works
1. Start with an empty solution.
2. Make a possible choice.
3. Check whether the choice is valid.
4. If valid, continue building the solution.
5. If invalid, undo the choice.
6. Try another possibility.
7. Stop when a complete solution is found or all possibilities have been explored.

"""

def find_sum(numbers, target, index=0, path=[]):

    if target == 0:
        print(path)
        return

    if target < 0 or index == len(numbers):
        return

    # Choose current number
    find_sum(
        numbers,
        target - numbers[index],
        index + 1,
        path + [numbers[index]]
    )

    # Skip current number
    find_sum(numbers, target, index + 1, path)


find_sum([2, 3, 5], 5)