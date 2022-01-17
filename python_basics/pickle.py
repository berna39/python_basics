import pickle
import random

results = ['win', 'lose', 'draw']
teams = ['liecster', 'arsenal', 'norwich', 'brighton']

premier_league = []

for t in teams:
    team_score = {}
    team_score[t] = 0
    for i in range(1,3):
        res = random.choice(results)
        if res == 'win':
            team_score[t] += 3
        elif res == 'draw':
            team_score[t] += 1
    premier_league.append(team_score)

with open('scores.txt', 'wb') as file:
    backup = pickle.Pickler(file)
    backup.dump(str(premier_league))
    
print(premier_league)
    
     

