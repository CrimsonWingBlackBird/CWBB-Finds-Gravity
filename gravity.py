from star import Star
from vector2D import Vector2D
import itertools
import random
import math


class Gravity():

    def gravity(star1: Star, star2: Star):
        bigG = 6.674e-3
        directionVector = star2.position - star1.position
        force = bigG * directionVector * \
            (star1.mass * star2.mass) / directionVector.mag() ** 3
        star1.acceleration += force / star1.mass
        star2.acceleration -= force / star2.mass


starList = []


# Initializes the environment.
def initialize():
    global starList
    numberOfStars = 50
    for star in range(numberOfStars):
        mass = random.uniform(0.1, 500)
        position = Vector2D(random.randint(250, 750), random.randint(250, 750))
        velocity = Vector2D(random.uniform(-0.5, 0.5),
                            random.uniform(-0.5, 0.5))
        newStar = Star(mass, position)
        newStar.velocity = velocity
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

# Merges stars.


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
                    bigStar.radius:
                newStar = combos[0].merge(combos[1])
                starList.remove(combos[0])
                starList.remove(combos[1])
                starList.append(newStar)


def destroy_distant_stars():
    global starList
    starList_copy = starList.copy()
    for star in starList_copy:
        if (star.position - Vector2D(500, 500)).mag() >= 1500:
            starList.remove(star)


def simulation(canvas):
    destroy_distant_stars()
    attract()
    updatePosition(canvas)
    previousLength = 0
    currentLength = len(starList)
    while previousLength != currentLength:  # Merges stars until stable
        mergeStars()
        previousLength = currentLength
        currentLength = len(starList)
