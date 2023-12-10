import loader

def minMinutes(L, mins):
    """Takes in a list L and a minimum number of minutes. Returns new list
    that does not include songs listened to for less than mins"""
    newL = []
    for i in L:
        if i[0] >= mins:
            newL.append(i)
    return newL

def sortByDate(L):
    """Takes in a list L and changes each data set to be of form
    [date, mins, title, artist] (swaps first two) so when sorted it sorts by date"""
    newL = []
    for i in L:
        mins, date, title, artist = i[0], i[1], i[2], i[3]
        newL.append([date, mins, title, artist])
    return newL

def sortByArtists(L, artists):
    #whitelists
    """Takes in list of data sets and a list of artists and returns L of only their data"""
    newL = []
    for i in L:
        mins, date, title, artist = i[0], i[1], i[2], i[3]
        if artist in artists:
            newL.append([mins, date, title, artist])
    return newL

def removeArtists(L, artists):
    #blacklists
    """Takes in list of data sets and list of artists and returns L without artists data"""
    newL = []
    for i in L:
        mins, date, title, artist = i[0], i[1], i[2], i[3]
        if artist not in artists:
            newL.append([mins, date, title, artist])
    return newL

def getTotalMins(L):
    """Takes in list of data sets and returns the total minutes"""
    totalMinutes = 0
    for i in L:
        mins = i[0]
        totalMinutes += mins
    return totalMinutes

def getTotalArtists(L):
    """Takes in list of data sets and returns total number of artists"""
    totalArtists = 0
    prevArtists = []
    for i in L:
        artist = i[3]
        if artist not in prevArtists:
            prevArtists.append(artist)
            totalArtists += 1
    return totalArtists

def getTotalSongs(L):
    """Takes in list of data sets and returns total number of songs"""
    totalSongs = 0
    for i in L:
        totalSongs += 1
    return totalSongs

def main():
    """Main program, calls all functions above and gets song data from loader"""
    songs = loader.load() #songs is list of form [[minutes, date, title, artist]]
    songs = minMinutes(songs, 0)
    #songs = removeArtists(songs, ["Michael Jackson", "Bladee", "Ecco2k", "Thaiboy Digital", "Drain Gang Archive", "Nirvana",
    #                              "Yung Lean", "Dj Billybool", "Xavier Wulf", "Cartier God", "dose", "Tapet", "Varg²™", "Woesum",
    #                              "Lady Gaga", "The Jacksons", "Ozzy Osbourne", "Black Sabbath"])
    totalMinutes = getTotalMins(songs)
    totalArtists = getTotalArtists(songs)
    totalSongs = getTotalSongs(songs)

    #Note: always call sortByDate last since it changes the index of data
    #songs = sortByDate(songs) #comment this out to sort by mins
    loader.print(songs, totalMinutes, totalArtists, totalSongs)

main()
