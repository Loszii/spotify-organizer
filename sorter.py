import loader

def minDate(L, date):
    """Takes in a list L and minimum date. Returns new list that does not
    inlcude songs listened to before that date"""
    newL= []
    for i in L:
        if i[1] >= date:
            newL.append(i)
    return newL

def maxDate(L, date):
    """Takes in a list L and max date. Returns new list that does not
    inlcude songs listened to after that date"""
    newL= []
    for i in L:
        if i[1] <= date:
            newL.append(i)
    return newL

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
    songs = loader.load() #songs is list of form [[minutes, first listened, title, artist], ...]
    songs = minMinutes(songs, 30) #enter minimum minutes listened here
    songs = removeArtists(songs, ["", None]) #enter blacklisted artists in list
    #songs = sortByArtists(songs, [""]) #uncomment to use whitelist and enter artists in list
    songs = minDate(songs, "0000-00-00") #enter minimum date here
    songs = maxDate(songs, "2023-12-29") #enter maximum date here
    totalMinutes = getTotalMins(songs)
    totalArtists = getTotalArtists(songs)
    totalSongs = getTotalSongs(songs)

    #songs = sortByDate(songs) #uncomment this to sort by date
    loader.print(songs, totalMinutes, totalArtists, totalSongs)

main()
