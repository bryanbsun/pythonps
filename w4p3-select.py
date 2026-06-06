# 
# Python Problem Solver
# Week 4 Problem 3: Song Selector
#

import time
import os

# Show the metronome
def metronome(bpm, timeSignature):
   beatInterval = 60 / bpm
   beatsPerMeasure = timeSignature.split('/')[0]

   while True:
      for beat in range(1, int(beatsPerMeasure) + 1):
         if beat == 1:
            os.system("clear")
            print("*** Metrononome App ***")
            print("----------------------")
            print("BPM: "+ str(bpm))
            print("Time Signature: "+ str(timeSignature))
            print("----------------------")
            print("> tick (" + str(beat) + ")")
         else:
            print("> tock (" + str(beat) + ")")
         time.sleep(beatInterval)

# Load from .csv file into a dictionary
def loadsongs(filename):
    # Create a dictionary
    d = {}
    with open(filename) as file:
        for line in file:
            l = line.split(",")
            # song name is the key, value is a tuple of (band, bpm, signature)
            d[l[0]] = l[1],l[2],l[3]
    return d

#Main Program Starts Here...
print("*** Metrononome App ***")
print("----------------------")
print("Option 1: Manul input")
print("Option 2: Search song name")

o = int(input())
while o != 1 and o != 2:
    o = int(input())

if o == 1:
    bpm = int(input("Enter BPM: "))
    timeSignature = input("Enter time signature (e.g., 4/4): ")
elif o == 2:
    songs = loadsongs("w4p3-rock-songs.csv")
    songname = input("Input song name:")
    while songname not in songs:
        songname = input("Input song name:")
    bpm = int(songs[songname][1])
    timeSignature = songs[songname][2]

metronome(bpm, timeSignature)

