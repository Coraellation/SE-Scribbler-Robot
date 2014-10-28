__author__ = 'George'

from myro import *
from random import randint
init("COM3")

#Anger
anger = ["darn", "wall in the way", "I dont like this wall", "wall you inconvenience", "wall move out of the way", "this wall dough", "why you block me"]

timewait = 0.5
spd = 0.8
tint = 0.5
rightturn = 0.33
leftturn = 0.64
tracker = 0


def approachWall():
    while (getObstacle("middle")==0):
        forward(spd)
    stop()
    print (getObstacle("middle"))
    forward(0.3, 0.1)
    speak("Oh a wall", 0)

def followWall():
    global tracker
    while (getObstacle("middle") != 0):

        timer = 0
        while (getObstacle("middle")):
            timer += 1
            move(0, -1)
        stop()
        print(timer)
        if (timer>3):
            turnRight(1, rightturn)
        else:
            turnRight(1, rightturn +0.18)
        wait(timewait)
        forward(spd, tint)
        wait(timewait)
        turnLeft(1, leftturn)
        wait(timewait)
        print getObstacle("middle")
        wait(timewait)
        tracker += 1
    speak ("I'm too wide", 0)

def turnCorner():
    turnRight(1, 0.78)

    while(getObstacle("middle") == 0):
        move(1, 0.75)
    stop()
    speak("next wall", 0)
    turnLeft(1, 0.25)

def turnCorner2():
    turnRight(1, 0.76)

    forward(1, 0.5)
    wait(timewait)
    turnLeft(1, leftturn)


approachWall()
followWall()
turnCorner()
followWall()
turnCorner2()
tracker /= 2
forward(spd, tint*tracker)
turnRight(1, 0.65)

#hand motion sto[p
while (getObstacle("middle")==0):
    move(1, 0)
stop()


