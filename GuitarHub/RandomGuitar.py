#Random Guitar Selector

#use random to generate a random note
import random

#use time to print the randomly generated note at intervals
#import time

base = ["A","B","C","D","E","F","G"]

flat = ["Ab","Bb","Db","Eb","Gb"]

sharp = ["A#","C#","D#","F#","G#"]

seventh = ["A7","B7","C7","D7","E7","F7","G7","Ab7","Bb7","Db7",
           "Eb7","Gb7","A#7","C#7","D#7","F#7","G#7"]



allNotes = base + flat + sharp
allChords = allNotes + seventh
#for i in base:
#    print(i)


print(" ")
print(random.choice(allNotes))
print(" ")
