"""
Definition
A greedy algorithm is an algorithmic strategy that makes the best possible choice at each step, 
hoping to achieve the overall best solution.

In simple language:

Choose what looks best right now without reconsidering previous decisions.
Example: Giving change
Suppose you need to give someone UGX 4,000 using denominations:
- UGX 2,000
- UGX 1,000
- UGX 500
A greedy algorithm selects the largest denomination possible at each step

"""

amount = 4000

denominations = [2000, 1000, 500]

for denomination in denominations:
    while amount >= denomination:
        amount -= denomination
        print("Use:", denomination)
        print("Remaining amount:", amount)

# test out this Suppose you have coins of 1, 3 and 4 units, and you need to make 6 units.














"""
amount = 6
denominations = [4, 3, 1]

for denomination in denominations:
    while amount >= denomination:
        amount -= denomination
        print("Use:", denomination)
        print("Remaining amount:", amount)
"""