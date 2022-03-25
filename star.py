from vector2D import Vector2D
import math


class Star():

    def __init__(self, mass: float, position: Vector2D):
        self.mass = mass
        self.position = position
        self.velocity = Vector2D(0, 0)
        self.acceleration = Vector2D(0, 0)
        self.radius = math.log(self.mass, 4)

    def merge(self, other):
        newMass = self.mass + other.mass
        newPosition = (self.position * self.mass
                       + other.position * other.mass) / newMass
        newVelocity = (self.velocity * self.mass
                       + other.velocity * other.mass) / newMass
        newStar = Star(newMass, newPosition)
        newStar.velocity = newVelocity
        newStar.radius = math.log(newStar.mass, 4)
        return newStar

    def show(self, canvas):
        radius = self.radius
        coord = (self.position.x - radius, self.position.y - radius,
                 self.position.x + radius, self.position.y + radius)
        canvas.create_oval(coord, fill="red")
