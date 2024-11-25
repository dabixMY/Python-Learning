# ──> Original import method:
# import random
# ──> Generate random choice using 'random.choice' method:
# coin = random.choice(["head", "tail"])

# ──> Updated import method: importing specific functions for clarity.
from random import choice, randint, shuffle

# ──> Generate a random choice between "head" and "tail".
# ──> Simplified with 'choice' directly, avoiding the need for 'random.' prefix.
coin = choice(["head", "tail"])

# ──> Print the result of the coin flip.
print(coin)

# ──> Generate a random integer between 1 and 10.
number = randint(1, 10)
print(number)

# ──> Shuffle a list of cards and print them.
cards = ["jack", "queen", "king"]
shuffle(cards)
for card in cards:
    print(card)
