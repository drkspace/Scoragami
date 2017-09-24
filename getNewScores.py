import csv
import sys
from pprint import pprint

import nflgame
import nflgame.update_sched


def teamNameConvert(tm):
    if tm == "JAX":
        tm = "JAC"
    if tm == "LAC":
        tm = "SD"
    if tm == "NYG":
        return "New York Giants"
    if tm == "NYJ":
        return "New York Jets" 
    
    for i in nflgame.teams:
        
        if tm == i[0]:
            return i[3]
        
def getNew(year, week):
    scores = []
    game = nflgame.games(year, week)
    for i in game:
        scores.append([str(year), str(week), teamNameConvert(i.away), str(i.score_away), teamNameConvert(i.home), str(i.score_home)])

    #pprint(scores)

    with open('scores.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            #print row
            #raw_input()
            if row in scores:
                print("{} already recorded".format(row))
                i = scores.index(row)
                del scores[i]

    with open('scores.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, lineterminator='\n')
        for i in scores:
            writer.writerow(i)

if __name__ == '__main__':
    year = int(sys.argv[1])
    week = int(sys.argv[2])
    getNew(year, week)
