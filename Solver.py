__author__ = 'George'
__project__ = 'test'

from myro import *
from random import randint
init("COM3")

#Anger
anger = ["darn it", "wall o m g", "I dont like this wall", "wall you bastard", "this wall is in the way", "this wall dough", "why you block me"]

#Stage 1: Move forward until obstacle detected
while (getObstacle("middle")==0):
    forward(0.8)
stop()
forward(0.3, 0.4)
print getObstacle("middle")
speak("holy shit a wall", 0)
#has detected something

while(getObstacle("middle")!=0):

    turnRight(1, 0.87)
    forward(0.8, 0.9)
    turnLeft(1, 0.71)
    print getObstacle("middle")
    r = randint(0, 6)
    speak(anger[r], 0)

#turn and move one last time cuz robot too fat
speak ("I'm fat", 0)
turnRight(1, 0.83)
forward(0.6, 0.5)
turnLeft(1, 0.71)

#hand motion sto[p
while (getObstacle("middle")==0):
    forward(0.8)
stop()