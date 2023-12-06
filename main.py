import json
import os

files = []
allSongs = {}
allSortedSongs = {}
mins = int(input("Enter minimum number of minutes listened (0 to see all data): "))
artists = []

for i in os.listdir(os.getcwd()):
    if "StreamingHistory" in i:
        files.append(json.load(open(i, encoding="utf-8")))

def minConvert():
    for i in allSongs:
        allSongs[i][0] = round(allSongs[i][0] / 60000, 1)

def getDate(current, prev):
    if prev == "":
        return current
    else:
        return prev

def initialize(data):
    for j in data:
        for i in j:
            allSongs[(i["trackName"], i["artistName"])] = [0, ""]
            #allSongs = (title, artist): [time, date]

def organize(data):
    for j in data:
        for i in j:
            allSongs[(i["trackName"], i["artistName"])] = [allSongs[(i["trackName"], i["artistName"])][0] + i["msPlayed"], getDate(i["endTime"], allSongs[(i["trackName"], i["artistName"])][1])]

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
        
def sortBySong(config):
    final = []
    allMinutes = round(getTotalMin())
    if config == "d":
        mode = "DATE"
        for i in allSortedSongs:
            if allSortedSongs[i][0] >= mins:
                final.append((allSortedSongs[i][1].split(" ")[0], allSortedSongs[i][0], i[0], i[1]))
                #final = [(date, time, title, artist), ...]
    else:
        mode = "MIN"
        for i in allSortedSongs:
            if allSortedSongs[i][0] >= mins:
                final.append((allSortedSongs[i][0], allSortedSongs[i][1].split(" ")[0], i[0], i[1]))
                #final = [(time, date, title, artist), ...]
    final.sort()
    txt = open("output.txt", "w", encoding="utf-8")
    txt.write(f"SORTED BY {mode}\nAll Songs listened to for more than {mins} minutes:\n\nFirst Listened | Title | Artist | Minutes")
    txt.close()
    txt = open("output.txt", "a", encoding="utf-8")
    for i in final:
        if config == "d":
            txt.write(f"\n{i[0]} | {i[2]} | {i[3]} | {i[1]}")
        else:
            txt.write(f"\n{i[1]} | {i[2]} | {i[3]} | {i[0]}")
    txt.write(f"\n\nThe total number of songs listened to for more than {mins} minutes is {len(final)}")
    txt.write(f"\nThe total number of minutes within all data is {allMinutes} minutes, which is {round(allMinutes / 1440)} days\n\n")
    txt.close()


def sortByArtist(config):
    final = []
    dataPerArtist = {}
    #dataPerArtist = artist: (date, time)
    allArtists = getTotalArtist()
    for i in allSortedSongs:
        dataPerArtist[i[1]] = [0, ""]
    for i in allSortedSongs:
        dataPerArtist[i[1]] = [dataPerArtist[i[1]][0] + allSortedSongs[i][0], getDate(allSortedSongs[i][1], dataPerArtist[i[1]][1])]
    if config == "d":
        for i in dataPerArtist:
            if dataPerArtist[i][0] >= mins: 
                final.append((dataPerArtist[i][1].split(" ")[0], round(dataPerArtist[i][0], 1), i, round(dataPerArtist[i][0] / 60, 1))) #need to round again since floating points
                #final = [(date, min, artist, hour)...]
    else:
        for i in dataPerArtist:
            if dataPerArtist[i][0] >= mins: # 
                final.append((round(dataPerArtist[i][0], 1), dataPerArtist[i][1].split(" ")[0], i, round(dataPerArtist[i][0] / 60, 1))) #need to round again since floating points
                #final = [(min, date, artist, hour)...]
    final.sort()
    txt = open("output.txt", "a", encoding="utf-8")
    txt.write("-------------------------------------------------\n" * 5)
    txt.write(f"\nAll artists listened to for more than {mins} minutes:\n\nFirst Listened | Artist | Minutes | Hours")
    for i in final:
        if config == "d":
            txt.write(f"\n{i[0]} | {i[2]} | {i[1]} | {i[3]}")
        else:
            txt.write(f"\n{i[1]} | {i[2]} | {i[0]} | {i[3]}")
    txt.write(f"\n\nThe total number of artists listened to for more than {mins} minutes is {len(final)}")
    txt.write(f"\nThe total number of artists within all data is {allArtists}")
    txt.close()

initialize(files)
organize(files)
minConvert()

def filterSongs(config):
    #allSongs = (title, artist): [time, date]
    if config == "b":
        for i in allSongs:
            if i[1] not in artists:
                allSortedSongs[i] = allSongs[i]
    elif config == "w":
        for i in allSongs:
            if i[1] in artists:
                allSortedSongs[i] = allSongs[i]
                


def getArtFilter():
    while True:
        option = input("Enter \"b\" to set to blacklist or \"w\" to set to whitelist\n")
        if option == "b":
            return "b"
        elif option == "w":
            return "w"

def artistMenu():
    config = getArtFilter()
    while True:
        option = input("Enter artist to blacklist or whitelist (HIT ENTER TO SKIP/FINISH)\n")
        if option == "":
            break
        else:
            artists.append(option.strip())
    filterSongs(config)

def menu():
    artistMenu()
    while True:
        option = input("Enter \"d\" to sort by date or \"m\" to sort by minutes\n")
        if option == "d":
            sortBySong(option)
            sortByArtist(option)
            return
        elif option == "m":
            sortBySong(option)
            sortByArtist(option)
            return
menu()
