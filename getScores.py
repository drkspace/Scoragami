from subprocess import call
import csv

url = "http://www.jt-sw.com/football/pro/results.nsf/Weeks/"
startYear = 1920
endYear = 2016
weeks = [str(i) for i in range(1,18)]
postLab = ["wc", "div", "conf", "sb"]
ext = weeks+postLab

for i in range(len(ext)):
    if len(ext[i])==1:
        ext[i]="0"+ext[i]

for year in range(startYear,endYear+1):
    print("Year - {}".format(year))
    for week in ext:
        w_url = url+str(year)+"-"+week
        call(["wget", "-P", "scores/", w_url])
