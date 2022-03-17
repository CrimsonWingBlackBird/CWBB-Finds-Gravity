from star import Star
from vector2D import Vector2D


class Gravity():

    def gravity(star1: Star, star2: Star):
        bigG = 6.674e-11
        distance = star1.mag(star2)
        force = bigG * (star1.mass * star2.mass) / (distance ** 2)

        star1.acceleration += (force / star1.mass)
        star2.acceleration += (force / star2.mass)
