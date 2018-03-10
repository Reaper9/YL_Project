class Vec2:

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __add__(self, other):  # Broken
        return Vec2(self.x + other.getX(), self.y + other.getY())

    def __mul__(self, other):
        return Vec2(self.x * other, self.y * other)

    def __sub__(self, other):
        return Vec2(self.x - other.getX(), self.y - other.getY())

    def __floordiv__(self, other):
        return Vec2(self.x // other.getX(), self.y // other.getY())

    def __truediv__(self, other):
        return Vec2(self.x / other, self.y / other)

    def add(self, other):
        self.x += other.getX()
        self.y += other.getY()

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, newX):
        self.x = newX

    def setY(self, newY):
        self.y = newY

    def __str__(self):
        return str(self.x) + ', ' + str(self.y)

    def getLength(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def normalize(self):
        length = self.getLength()
        return Vec2(self.x / length, self.y / length)

    def normalizeThis(self):
        length = self.getLength()
        self.x /= length
        self.y /= length