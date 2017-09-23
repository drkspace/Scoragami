from bs4 import BeautifulSoup
from os import listdir
from pprint import pprint
import csv
from copy import copy


def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def scores_to_list(scores):
    score = []
    for i in scores:
        i = list(i)
        #print(''.join(copy(i)))
        c = i.index(',')
        
        def split(ts):
            if isInt(ts[len(ts)-2]):
                s = int(''.join(ts[-2:]))
                del ts[-3:]
            else:
                s = int(''.join(ts[-1:]))
                del ts[-2:]

            return [''.join(ts),s]

        score.append([split(i[0:c]), split(i[c+1:])])
    return score

def f_to_y_w(f):
    f=list(f)
    d = f.index('-')
    return ''.join(f[0:d]), ''.join(f[d+1:])


folder = "scores"

files = listdir(folder)
for j in range(len(files)):
    doc = folder + "/" + files[j]
    print files[j]

    with open(doc, 'r') as myfile:
        data=myfile.read()#.replace('\n', '')

    soup = BeautifulSoup(data, 'html.parser')
    tag = soup.a

    scores = []
    for i in soup.find_all('ul'):
        
        s = list(i.get_text())
        for _ in range(17):
            try:
                tmp = ''.join(copy(s))
                b = tmp.index('Bye:')
                n = tmp.find('\n', b)
                del s[b:n+1]
            except:
                pass

            try:
                tmp = ''.join(copy(s))
                at = tmp.index(' at ')
                cmma = tmp.find(',', at)+3
                if cmma-at > 30:
                    del s[at:at+len(" at Giants Stadium")]
                    continue
                del s[at:cmma]
            except:
                pass

        
            try:
                tmp = ''.join(copy(s))
                at = tmp.index(" -- Box Score")
                del s[at:at+len(" -- Box Score")]
            except :
                pass

            try:
                tmp = ''.join(copy(s))
                at = tmp.index(" (OT) ")
                del s[at:at+len(" (OT) ")]
            except :
                pass
        
        #print(''.join(copy(s)))
        last = 0
        for k in range(len(s)):
            if isInt(s[k]):
            
                try:
                    if  (isInt(s[k+1]) or s[k+1] == ',' or s[k+1] == 'e'):
                    
                        continue
                    else:
                        scores.append(''.join(s[last:k+1]))
                        last=k+1
                except:
                    scores.append(''.join(s[last:k+1]))
        break
    scores = scores_to_list(scores)
    y, w = f_to_y_w(files[j])

    for i in scores:
    
        with open('scores.csv', 'a') as csvfile:
            writer = csv.writer(csvfile, lineterminator='\n')
            writer.writerow([y, w, i[0][0], i[0][1], i[1][0], i[1][1]])

