from star import Star
from vector2D import Vector2D
import itertools
import random
from gravity import Gravity
import math


starList = []


# Initializes the environment.
def initialize():
    global starList
    numberOfStars = 50
    for star in range(numberOfStars):
        mass = random.randint(1, 500)
        position = Vector2D(random.randint(0, 500),
                            Vector2D(random.randint(0, 500)))
        newStar = Star(mass, position)
        starList.append(newStar)


# Performs attraction between stars.
def attract():
    global starList
    combinationList = itertools.combinations(starList, 2)
    for combo in combinationList:
        Gravity.gravity(combo[0], combo[1])


# Updates the star's position and velocity, resets accel to 0.
def updatePosition(star: Star):
    star.velocity += star.acceleration
    star.acceleration = Vector2D(0, 0)
    star.position += star.velocity


def mergeStars():
    global starList
    combinationList = itertools.combinations(starList, 2)
    for combos in combinationList:
        if combos[0].mass >= combos[1].mass:
            bigStar = combos[0]
        else:
            bigStar = combos[1]
        if combos[0].position.distance(combos[1].position) >= \
                math.log(bigStar.mass, 4):
            newStar = combos[0].merge(combos[1])
            starList.remove(combos[0])
            starList.remove(combos[1])
            starList.append(newStar)
