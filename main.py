"""Project name :  Dictionary and Sets training
    File name : main.py
    Programmer : Colin B. Chin Choy
"""

SongDict = {"SongName" : "Begin Again", "ReleaseDate" : "1/10/2012", "Label" : "Big Machine", "Artist" : "Taylor Swift", "Genre" : "Country", "SongWriter" : "Taylor Swift"}
print ("\n"*50)
print("-----------------------------------*----------------------------------")
for sd in SongDict :
    print(sd,SongDict[sd])
print("-----------------------------------*----------------------------------")
input("Press Enter to do a quiz on what you say")
print ("\n"*50)

def quiZSongs():
    for sd in SongDict :
        print("-----------------------------------*----------------------------------")
        an = str(input("What is the "+sd+" : "))
        an1 = an.lower()
        sda = SongDict[sd].lower()
        if an1 == sda :
            print("True - "+sd+" is "+str(SongDict[sd]))
        else:
            print("False - "+sd+" is "+str(SongDict[sd]))

quiZSongs()
