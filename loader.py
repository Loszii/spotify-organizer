import json
import os

def storeFiles():
    """Opens each file in current directory with Streaming_History in name
    Then appends to a files list after using json.load to convert to python object"""
    files = []
    for i in os.listdir(os.getcwd()):
        if "Streaming_History" in i:
            files.append(json.load(open(i, encoding="utf-8")))
    return files

def storeDict(L):
    """Takes in list parameter of files (each file is list of dicts) and return
    dictionary of songs. Dict form: (track, artist): (ms, first listened)"""
    songs = {}
    for i in L: #i is a Streaming_History list from main list of files
        for j in i: #j is a dict in the sub list
            songs[(j["master_metadata_track_name"], j["master_metadata_album_artist_name"])] = [0, []]
    for i in L:
        for j in i:
            prevMS = songs[(j["master_metadata_track_name"], j["master_metadata_album_artist_name"])][0]
            newMS = prevMS + j["ms_played"]
            prevDates = songs[(j["master_metadata_track_name"], j["master_metadata_album_artist_name"])][1]
            newDates = prevDates + [j["ts"]]
            songs[(j["master_metadata_track_name"], j["master_metadata_album_artist_name"])] = [newMS, newDates]
    for i in songs:
        dates = songs[i][1]
        newDates = min(dates)
        songs[i][1] = newDates
    return songs

def storeSongs(D):
    """Takes in a dictionary with keys of tuples whose values are time and date,
    appends each songs data to a list and returns"""
    songs = []
    for i in D:
        title = i[0]
        artist = i[1]
        ms = D[i][0]
        date = D[i][1]
        newDate = date.split("T")[0]
        minutes = round(ms / 60000)
        songs.append([minutes, newDate, title, artist])
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