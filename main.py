import json
import os

files = []
allSongs = {}

for i in os.listdir(os.getcwd()):
    if "StreamingHistory" in i:
        files.append(json.load(open(i, encoding="utf-8")))

def minConvert():
    for i in allSongs:
        allSongs[i][0] = round(allSongs[i][0] / 60000, 1)

def getDate(i):
    if allSongs[i["trackName"], i["artistName"]][1] == "":
        return i["endTime"]
    else:
        return allSongs[i["trackName"], i["artistName"]][1]

def initialize(data):
    for j in data:
        for i in j:
            allSongs[(i["trackName"], i["artistName"])] = [0, ""]
            #(title, artist): [time, date]

def organize(data):
    for j in data:
        for i in j:
            allSongs[(i["trackName"], i["artistName"])] = [allSongs[(i["trackName"], i["artistName"])][0] + i["msPlayed"], getDate(i)]

def getTotalMin():
    count = 0
    for i in allSongs:
        count += allSongs[i][0]
    return count

def getTotalArtist():
    memory = {}
    count = 0
    for i in allSongs:
        if i[1] not in memory:
            count += 1
            memory[i[1]] = True
    return count
        

def sortByTotal():
    final = []
    allMinutes = round(getTotalMin())
    mins = int(input("Enter minimum number of minutes listened (0 to see all data): "))
    for i in allSongs:
        if allSongs[i][0] >= mins:
            final.append((allSongs[i][1].split(" ")[0], allSongs[i][0], i[0], i[1]))
            #final = [(date, time, title, artist), ...]
    final.sort()
    txt = open("output.txt", "w", encoding="utf-8")
    txt.write(f"All Songs listened to for more than {mins} minutes:\n\nFirst Listened | Minutes | Title | Artist")
    txt.close()
    txt = open("output.txt", "a", encoding="utf-8")
    for i in final:
        txt.write(f"\n{i[0]} | {i[1]} | {i[2]} | {i[3]}")
    txt.write(f"\n\nThe total number of songs listened to for more than {mins} minutes is {len(final)}")
    txt.write(f"\nThe total number of minutes within all data is {allMinutes} minutes, which is {round(allMinutes / 24)} days")
    txt.close()

def sortByArtist():
    minPerArtist = {} #artist: time
    final = []
    mins = int(input("Enter minimum number of minutes listened (0 to see all data): "))
    for i in allSongs:
        minPerArtist[i[1]] = 0
    for i in allSongs:
        minPerArtist[i[1]] += allSongs[i][0]
    for i in minPerArtist:
        if minPerArtist[i] >= mins:
            final.append((round(minPerArtist[i], 1), round(minPerArtist[i] / 60, 1), i)) #need to round again since floating points
            #final = [(min, hour, artist)...]
    allArtists = getTotalArtist()
    final.sort()
    txt = open("output.txt", "w", encoding="utf-8")
    txt.write(f"All artists listened to for more than {mins} minutes:\n\nArtist | Minutes | Hours")
    for i in final:
        txt.write(f"\n{i[2]} | {i[0]} | {i[1]}")
    txt.write(f"\n\nThe total number of artists listened to for more than {mins} minutes is {len(final)}")
    txt.write(f"\nThe total number of artists within all data is {allArtists}")
    txt.close()

#function calls
initialize(files)
organize(files)
minConvert()

def menu():
    option = input("Enter \"t\" for total stats\nEnter \"a\" to see minutes per artists\nEnter \"w\" to whitelist artists\nEnter \"b\" to blacklist artists\nEnter anything else to quit\n")
    if option == "t":
        sortByTotal()
    elif option == "a":
        sortByArtist()
    elif option == "w":
        pass #implement
    elif option == "b":
        pass #implement
    else:
        exit()
menu()