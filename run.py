import sys
from getNewScores import getNew as gn
from chart import chart

if len(sys.argv) > 1:
    gn(int(sys.argv[1]), int(sys.argv[2]))
chart()

