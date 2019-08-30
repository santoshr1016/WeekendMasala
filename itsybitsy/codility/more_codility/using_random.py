import random
import itertools
import sys

dice = random.randrange(1,7)
print("You rolled: " + str(dice))

lottery_winners = random.sample(range(1, 100), 5)
print(lottery_winners)

possible_pets = ["cats", "dogs", "fish"]
print(random.choice(possible_pets))

cards = ["King", "Queen", "Jack", "Ace"]
random.shuffle(cards)
print(cards)

num = [1,2,3]
for p in itertools.permutations(num):
    print(p)

names = {1: "San", 2: "Tosh", 3: "Shru"}
for p in itertools.permutations(names.values()):
    print(p)

print("Number of Args: ", len(sys.argv))
print("Args: ", sys.argv)
