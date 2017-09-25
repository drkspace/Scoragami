import csv
from copy import deepcopy
from pprint import pprint

import plotly.figure_factory as ff
import plotly.graph_objs as go
import plotly.plotly as py


def chart():

    scores = []

    with open('scores.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row)==0:
                continue
            tmp = [int(row[3]), int(row[5])]
            if tmp[1] > row[0]:
                tmp.reverse()
            tmp.append(row[0]+" Week "+row[1]+", "+row[2]+" at "+row[4])
            scores.append(tmp)

    #pprint(scores)
    hmap = []
    for i in range(0,74):
        for k in range(0,74):
            hmap.append([i, k, 0, "Games:<br>"])
    #pprint(hmap)

    for s in scores:
        for i in range(len(hmap)):

            if [s[0],s[1]] == [hmap[i][0],hmap[i][1]]:
                #print(1)
                hmap[i][2]+=1
                #print hmap[i][2]
                hmap[i][3]+=s[2]+"<br>"

    #pprint(hmap)

    row=[0 for i in range(75)]
    text = [[deepcopy(row)]*74 for i in range(75)]
    hm_z = [[row]*74 for i in range(75)]
    for i in hmap:

        if i[1]>i[0] or (i[0]==1 and i[1]<=1) or (i[1]==1 and i[0]<=7 and i[0]!=6):
            hm_z[i[0]][i[1]] = -1
            continue


        hm_z[i[0]][i[1]] = i[2]
        text[i[0]][i[1]] = i[3]


    solid_z = deepcopy(hm_z)
    for i in range(len(solid_z)):

        for k in range(len(solid_z[i])):
            if solid_z[i][k] > 0:
                if i == 74:
                    solid_z[i][k] = 0 #Need to change if a team scores 74
                    continue        
                solid_z[i][k] = 100

    for i in range(len(text)):
        for k in range(len(text[i])):
            if len(text[i][k])>3000:
                text[i][k] = "Too many games"

    axis = [i for i in range(0,75)]

    trace = go.Heatmap(z=hm_z, x=axis, xgap=2, ygap=2, y=axis,
                         colorscale = [[0,'rgb(255,255,255)'],[1,'rgb(0,0,0)']], 
                         name = "Scoragami", autocolorscale = False, zmin=0, 
                         hoverinfo="x+y+z+text", text=text, showlegend=False)

    data = [trace]

    py.plot(data, filename="heatmap")

    for i in range(len(hm_z)):
        for k in range(len(hm_z[i])):
            text[i][k] = "Z: "+str(hm_z[i][k])+"<br>"+str(text[i][k])
            if "[" in text[i][k]:
                text[i][k] = "Score not possible"

    trace2 = go.Heatmap(z=solid_z, x=axis,xgap=2,x0=-.5, ygap=2, y=axis,
                         colorscale = [[0,'rgb(255,255,255)'],[1,'rgb(0,0,0)']],
                         name = "Solid Scoragami", autocolorscale = False, zmin=0, 
                         hoverinfo="x+y+text", text=text, showlegend=False)

    data2 = [trace2]

    py.plot(data2, filename="Solid Heatmap")

if __name__ == "__main__":
    chart()
