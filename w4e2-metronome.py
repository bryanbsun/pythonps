# 
# Python Problem Solver
# Week 4 Example 2: Metronome App
#

import time
import os

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

#Main Program Starts Here...
print("*** Metrononome App ***")
print("----------------------")
bpm = int(input("Enter BPM: "))
timeSignature = input("Enter time signature (e.g., 4/4): ")
metronome(bpm, timeSignature)

