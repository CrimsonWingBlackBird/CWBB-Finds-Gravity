from star import Star
from vector2D import Vector2D
import itertools
import random
import math


class Gravity():

    def gravity(star1: Star, star2: Star):
        bigG = 6.674e-3
        distance = star1.position.distance(star2.position)
        force = bigG * (star1.mass * star2.mass) / (distance ** 2)

        acccelDirection = (star2.position - star1.position).normalize()
        star1.acceleration += (force / star1.mass)*acccelDirection
        star2.acceleration += (force / star2.mass)*(-acccelDirection)


starList = []


# Initializes the environment.
def initialize():
    global starList
    numberOfStars = 50
    for star in range(numberOfStars):
        mass = random.randint(1, 500)
        position = Vector2D(random.randint(0, 500), random.randint(0, 500))
        newStar = Star(mass, position)
        starList.append(newStar)


# Performs attraction between stars.
def attract():
    global starList
    combinationList = itertools.combinations(starList, 2)
    for combo in combinationList:
        Gravity.gravity(combo[0], combo[1])


# Updates the star's position and velocity, resets accel to 0.
def updatePosition(canvas):
    global starList
    for star in starList:
        star.velocity += star.acceleration
        star.acceleration = Vector2D(0, 0)
        star.position += star.velocity
        star.show(canvas)


def mergeStars():
    global starList
    combinationList = itertools.combinations(starList, 2)
    for combos in combinationList:
        if combos[0] in starList and combos[1] in starList:
            if combos[0].mass >= combos[1].mass:
                bigStar = combos[0]
            else:
                bigStar = combos[1]
            if combos[0].position.distance(combos[1].position) <= \
                    math.log(bigStar.mass, 4):
                newStar = combos[0].merge(combos[1])
                starList.remove(combos[0])
                starList.remove(combos[1])
                starList.append(newStar)


def simulation(canvas):
    attract()
    updatePosition(canvas)
    previousLength = 0
    currentLength = len(starList)
    while previousLength != currentLength:  # Merges stars until stable
        mergeStars()
        previousLength = currentLength
        currentLength = len(starList)
