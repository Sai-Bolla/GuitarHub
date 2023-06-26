import RandomGuitar
import random

#first ask the question
#create the fretboard with the note query
#take in input and validate the answer

#this is the list of notes on the fretboard
listNotes = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
globalNote = ""
globalString = ""

#function prints question
def askQuestion():
    formatNote = ["1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th"]
    formatString = ["1st","2nd","3rd","4th","5th","6th"]
    note = random.choice(formatNote)
    guitarString = random.choice(formatString)
    print("What is the note on the %s fret of the %s string?" %(note,guitarString))

    outputNote = note[:-2]
    outputString = guitarString[0]
    return (outputNote,outputString)

#funciton that prints the guitar board using input of note and string
def printBoard(note,guitarString):
    start = "|"
    segment = "---|"
    choice = "-x-|"

    topline = "0---1---2---3---4---5---6---7---8---9---10--11--12"
    columnline = ["e","B","G","D","A","E"]
    print(topline)
    print("")
    for i in range(6):
        line = ""
        line += columnline[i]
        if note == "1":
            line += "x"
        else:
            line += start
        for j in range(1,13):
            if i == (guitarString - 1) and j == (note):
                line += choice
            elif note == "12":
                line += "X"
            else:
                line += segment

        print(line)
    print("")

def checkAnswer(input,note,guitarString):




    #use a TRY CATCH exception if possible
    



    
    eString = ["F","F#","G","G#","A","A#","B","C","C#","D","D#","E"]
    BString = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
    GString = ["G#","A","A#","B","C","C#","D","D#","E","F","F#","G"]
    DString = ["D#","E","F","F#","G","G#","A","A#","B","C","C#","D"]
    AString = ["A#","B","C","C#","D","D#","E","F","F#","G","G#","A"]
    EString = ["F","F#","G","G#","A","A#","B","C","C#","D","D#","E"]

    strings = [eString,BString,GString,DString,AString,EString]
    
    # 'clean' input for spaces and case

    input = input.upper()
    input = input.replace(" ","")

    try:
        correct = strings[int(guitarString)-1][int(note)-1]
        print(note+ " " + guitarString)
        #correct = strings[int(note)][int(guitarString)]

        
        
        if input == correct:
            print("correct!")
        else:
            print("not correct! "+ correct)

            print(strings)
    except Exception as error:
        print("input not valid:",error)



globalNote,globalString = askQuestion()
print("")

printBoard(int(globalNote),int(globalString))

answer = str(input())

checkAnswer(answer,globalNote,globalString)
