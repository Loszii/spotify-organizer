import loader
#To do: add getTotalMins(), getTotalArtists(), getTotalSongs()
def minMinutes(L, mins):
    """Takes in a list L and a minimumn number of minutes and takes out 
    each data set (list) in list that has less time listened than mins"""
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
        mins = i[0]
        date = i[1]
        title = i[2]
        artist = i[3]
        newL.append([date, mins, title, artist])
    return newL

def sortByArtists(L, artists):
    #whitelists
    """Takes in list of data sets and a list of artists and returns L of only their data"""
    newL = []
    for i in L:
        mins = i[0]
        date = i[1]
        title = i[2]
        artist = i[3]
        if artist in artists:
            newL.append([mins, date, title, artist])
    return newL

def removeArtists(L, artists):
    #blacklists
    """Takes in list of data sets and list of artists and returns L without artists data"""
    newL = []
    for i in L:
        mins = i[0]
        date = i[1]
        title = i[2]
        artist = i[3]
        if artist not in artists:
            newL.append([mins, date, title, artist])
    return newL

def main():
    """Main program, calls all functions above and gets song data from loader"""
    #Note: edit artists before picking sorting mode
    songs = loader.load() #songs is list of form [[minutes, date, title, artist]]
    songs = minMinutes(songs, 15)
    songs = removeArtists(songs, ["Michael Jackson", "Bladee", "Ecco2k", "Thaiboy Digital", "Drain Gang Archive", "Nirvana",
                                  "Yung Lean", "Dj Billybool", "Xavier Wulf", "Cartier God", "dose", "Tapet", "Varg²™", "Woesum",
                                  "Lady Gaga", "The Jacksons", "Ozzy Osbourne", "Black Sabbath"])

    #songs = sortByDate(songs) #comment this out to sort by mins
    loader.print(songs)

main()
