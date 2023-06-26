
#Metronome function

import time

#how many blips to print per run
metronomeLength = 10

def askbpm():
    print("What bpm do you want the metronome?")
    bpm = input()

    try:
        bpm = int(bpm)
        print("input accepted")
        return bpm
    except:
        print("invalid input")

def Metronome(inputbpm):

    i = 0
    print("First blip")

    while i < metronomeLength:
        time.sleep(60/inputbpm)
        print("Blip")
        i += 1
    

bpm = askbpm()
Metronome(bpm)