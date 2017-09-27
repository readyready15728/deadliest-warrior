from __future__ import division
from collections import Counter
from random import random

# I know I'm hard-coding a bunch of stuff here but remember: premature
# optimization is the root of all evil
def deadliest_warrior():
    knight = {'hp': 300,
              'attack': 80,
              'defense': 30,
              'dodge': 0.9}
    monster = {'hp': 1500,
               'attack': 120,
               'defense': 60,
               'dodge': 0}

    while True:
        # Knight attack
        if random() < 1/3:
            attack_k = knight['attack'] * 3
        else:
            attack_k = knight['attack']

        if random() > monster['dodge']:
            monster['hp'] -= attack_k - monster['defense']

        # Monster attack
        if random() > knight['dodge']:
            if random() < 1/4:
                knight['hp'] = 0
            else:
                knight['hp'] = monster['attack'] - knight['defense']
        
        if knight['hp'] <= 0 and monster['hp'] <= 0:
            return 'both dead'
        elif knight['hp'] <= 0:
            return 'monster'
        elif monster['hp'] <= 0:
            return 'knight'
        
outcomes = Counter()

for _ in xrange(100000):
    outcomes[deadliest_warrior()] += 1

print outcomes
