from vector2D import Vector2D


class Star():

    def __init__(self, mass: float, position: Vector2D):
        self.mass = mass
        self.position = position
        self.velocity = Vector2D(0, 0)
        self.acceleration = Vector2D(0, 0)

    def merge(self, other):
        newMass = self.mass + other.mass
        newPosition = (self.position + other.position) / 2
        newVelocity = (self.velocity + other.velocity) / 2
        newStar = Star(newMass, newPosition)
        newStar.velocity = newVelocity
        return newStar
