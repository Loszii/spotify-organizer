import json
import os

#have total stats show number of artists listened to and number of songs listened to

blacklist = [] #artists to blacklist
files = []
# current black = ["Bladee", "Thaiboy Digital", "Ecco2k", "Drain Gang Archive", "Yung Lean", "Dj Billybool", "Michael Jackson", "Nirvana"]
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
            if i["artistName"] not in blacklist:
                allSongs[(i["trackName"], i["artistName"])] = [0, ""]
                #(title, artist): [time, date]

def organize(data):
    for j in data:
        for i in j:
            if i["artistName"] not in blacklist:
                allSongs[(i["trackName"], i["artistName"])] = [allSongs[(i["trackName"], i["artistName"])][0] + i["msPlayed"], getDate(i)]

def getTotalMin():
    count = 0
    for i in allSongs:
        count += allSongs[i][0]
    return count

def sortByArtist():
    minPerArtist = {} 
    #artist: time


    
    allMinutes = getTotalMin()
    txt = open("output.txt", "w", encoding="utf-8")
    #print alll minPerArtist


    txt.write(f"\n\nThe total number of minutes is {round(allMinutes)} minutes!")
    txt.close()

def sortByMin():
    final = []
    mins = int(input("Enter minimum number of minutes listened: "))
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
    txt.close()


#function calls
initialize(files)
organize(files)
minConvert()

def menu():
    option = input("Enter \"t\" for total stats\nEnter \"m\" to sort by minimum minutes listened\nEnter \"a\" to see minutes per artists\nEnter \"w\" to whitelist artist or \"b\" to blacklist\nEnter anything else to quit\n")
    if option == "t":
        pass
    elif option == "m":
        sortByMin()
    elif option == "a":
        sortByArtist()
    elif option == "w":
        pass
    elif option == "b":
        pass
    else:
        exit()
menu()