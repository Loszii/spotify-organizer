import json
import os

mins = 60
history = []
files = []
# current black = ["Bladee", "Thaiboy Digital", "Ecco2k", "Drain Gang Archive", "Yung Lean", "Dj Billybool", "Michael Jackson", "Nirvana"]
blacklist = [] #artists to blacklist
allSongs = {} #key: (title, artist) value: [time, date]
final = [] #final = (date, time, title, artist)
for i in os.listdir(os.getcwd()):
    if "StreamingHistory" in i:
        history.append(i)

for i in history:
    files.append(json.load(open(i, encoding="utf-8")))

def initialize(data):
    for i in data:
        if i["artistName"] not in blacklist:
            allSongs[(i["trackName"], i["artistName"])] = [0, ""]

def getDate(i):
    if allSongs[i["trackName"], i["artistName"]][1] == "":
        return i["endTime"]
    else:
        return allSongs[i["trackName"], i["artistName"]][1]

def organize(data):
    for i in data:
        if i["artistName"] not in blacklist:
            allSongs[(i["trackName"], i["artistName"])] = [allSongs[(i["trackName"], i["artistName"])][0] + i["msPlayed"], getDate(i)]
        
for i in files:
    initialize(i)
for i in files:
    organize(i)


for i in allSongs:
    allSongs[i][0] = round(allSongs[i][0] / 60000)
    if allSongs[i][0] >= mins:
        final.append((allSongs[i][1].split(" ")[0], allSongs[i][0], i[0], i[1]))
final.sort()
txt = open("output.txt", "w", encoding="utf-8")
for i in final:
    txt.write(f"{i[0]} | {i[1]} | {i[2]} | {i[3]} \n")
txt.close()
#final = date of first listen | mins listened | title | artist