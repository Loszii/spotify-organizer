#Returns a files list which is a list of dictionaries involving song data
import json
import os

def storeFiles():
    """Opens each file in current directory with StreamingHistory in name
    Then appends to a files list after using json.load to convert to python object"""
    files = []
    for i in os.listdir(os.getcwd()):
        if "StreamingHistory" in i:
            files.append(json.load(open(i, encoding="utf-8")))
    return files

def storeDict(L):
    """Takes in list parameter of files (each file is list of dicts) and return
    dictionary of songs. Dict form: (track, artist): (ms, first date)"""
    songs = {}
    for i in L: #i is a StreamingHistory list from main list of files
        for j in i: #j is a dict in the sub list
            songs[(j["trackName"], j["artistName"])] = [0, ""]
    for i in L:
        for j in i:
            prevMS = songs[(j["trackName"], j["artistName"])][0]
            prevDate = songs[(j["trackName"], j["artistName"])][1]
            newMS = prevMS + j["msPlayed"] #for each time listened to this song adds the ms played
            if prevDate == "": #if no date then this is first since history is sorted
                newDate = (j["endTime"].split())[0]
            else:
                newDate = prevDate
            songs[(j["trackName"], j["artistName"])] = (newMS, newDate)
    return songs

def storeSongs(D):
    """Takes in a dictionary with keys of tuples whose values are time and dates,
    appends each songs data to a list and returns"""
    songs = []
    for i in D:
        title = i[0]
        artist = i[1]
        ms = D[i][0]
        date = D[i][1]
        minutes = round(ms / 60000) #turns total ms to total mins
        songs.append([minutes, date, title, artist]) #songs will be a list of lists with this data in each
    return songs

def load():
    """Calls above functions and returns the list of songs"""
    return storeSongs(storeDict(storeFiles()))

def print(L, mins, artists, songs):
    """Takes in list L of lists and sorts it. Also takes in totalMins, totalArtists, and totalSongs
    Then prints them along with each element in the list"""
    days = round(mins / 1440)
    L.sort()
    txt = open("output.txt", "w", encoding="utf-8")
    txt.write(f"Total Minutes: {mins}\nTotal Days: {days}\nTotal Artists: {artists}\nTotal Songs: {songs}\n\n")
    for i in L:
        txt.write(f"{i[0]} | {i[1]} | {i[2]} | {i[3]}\n")
    txt.close()