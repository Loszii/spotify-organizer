import json
import os

mins = 10
history = []
files = []
blacklist = ["Bladee", "Thaiboy Digital", "Ecco2k", "Drain Gang Archive", "Yung Lean", "Dj Billybool", "Michael Jackson", "Nirvana"] #artists to blacklist
allSongs = {} #key: (title, artist) value: time
final = [] #final = (time, title, artist)
for i in os.listdir(os.getcwd()):
    if "StreamingHistory" in i:
        history.append(i)

for i in history:
    files.append(json.load(open(i, encoding="utf-8")))

def initialize(data):
    for i in data:
        if i["artistName"] not in blacklist:
            allSongs[(i["trackName"], i["artistName"])] = 0

def organize(data):
    for i in data:
        if i["artistName"] not in blacklist:
            allSongs[(i["trackName"], i["artistName"])] += i["msPlayed"]
        
for i in files:
    initialize(i)
for i in files:
    organize(i)

for i in allSongs:
    allSongs[i] = round(allSongs[i] / 60000)
    if allSongs[i] >= mins:
        final.append((allSongs[i], i[0], i[1]))

final.sort()
txt = open("output.txt", "w", encoding="utf-8")
for i in final:
    txt.write(f"{i[1]} | {i[2]} | {i[0]} \n")
txt.close()