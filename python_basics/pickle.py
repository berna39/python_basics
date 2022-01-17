import pickle
import random

results = ['win', 'lose', 'draw']
teams = ['liecster', 'arsenal', 'norwich', 'brighton', 'wolvwrampton', 'leeds', 'westham', 'new castle', 'crystal palace', 'manchester united', 'chelsea', 'watford', 'burnley']

premier_league = []

def play_matchs(team):
    team_score = {}
    team_score[team] = 0
    for i in range(1,3):
        res = random.choice(results)
        if res == 'win':
            team_score[team] += 3
        elif res == 'draw':
            team_score[team] += 1
    return team_score


for t in teams:
    premier_league.append(play_matchs(t))

#doing the backup of the premier league scores
with open('scores.txt', 'wb') as file:
    backup = pickle.Pickler(file)
    backup.dump(str(premier_league))
    
print(premier_league)

print('---------- retrieving data -----------')

with open('scores.txt', 'rb') as file:
    backup = pickle.Unpickler(file)
    premier_league = backup.load()
    print(premier_league)    
     

