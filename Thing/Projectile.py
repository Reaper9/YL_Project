from Thing.Thing import Thing
from doomConstants import *

class Projectile(Thing):

    def __init__(self, position, velocity, damage, doomMap):
        super(Projectile, self).__init__()
        self.doomMap = doomMap
        self.position = position
        self.velocity = velocity
        self.damage = damage
        self.destroyed = False

    def updateMovement(self, deltaTime, things):
        expectedPosition = self.position + self.velocity * deltaTime
        if self.doomMap:
            x, y = int(expectedPosition.getX()) + self.imageWidth // 2, int(
                expectedPosition.getY()) + self.imageHeight // 2
            if not self.doomMap.getCollision((x + self.imageWidth // 2) // MAP_TILE_WIDTH,
                                             y // MAP_TILE_HEIGHT) and not self.doomMap.getCollision(
                x // MAP_TILE_WIDTH,
                (y + self.imageHeight // 2) // MAP_TILE_HEIGHT) and not self.doomMap.getCollision(
                (x - self.imageWidth // 2) // MAP_TILE_WIDTH,
                y // MAP_TILE_HEIGHT) and not self.doomMap.getCollision(x // MAP_TILE_WIDTH, (
                                                                                                     y - self.imageHeight // 2) // MAP_TILE_HEIGHT):
                self.position = expectedPosition
            else:
                self.onWallHit()
            for thing in things:
                if thing.getType() == T_MONSTER:
                    tX, tY = int(thing.getPosition().getX() // MAP_TILE_WIDTH), (thing.getPosition().getY() // MAP_TILE_HEIGHT)
                    if tX == self.position.getX() // MAP_TILE_WIDTH and tY == self.position.getY() // MAP_TILE_HEIGHT:
                        thing.damage(self.damage)
        self.updateImage()

    def onWallHit(self):
        self.destroyed = True

    def isDestroyed(self):
        return self.destroyed

class Bullet(Projectile):

    def __init__(self, position, velocity, damage, doomMap):
        super(Bullet, self).__init__(position, velocity, damage, doomMap)
        self.image = 'bullet'
        self.updateImageParameters()

class Shell(Projectile):

    def __init__(self, position, velocity, damage, doomMap):
        super(Shell, self).__init__(position, velocity, damage, doomMap)
        self.image = 'shell'
        self.updateImageParameters()

class Rocket(Projectile):

    def __init__(self, position, velocity, damage, doomMap):
        super(Rocket, self).__init__(position, velocity, damage, doomMap)
        self.image = 'rocket'
        self.updateImageParameters()

class Plasma(Projectile):

    def __init__(self, position, velocity, damage, doomMap):
        super(Plasma, self).__init__(position, velocity, damage, doomMap)
        self.image = 'plasma'
        self.updateImageParameters()

class BFGProjectile(Projectile):

    def __init__(self, position, velocity, damage, doomMap):
        super(BFGProjectile, self).__init__(position, velocity, damage, doomMap)
        self.image = 'BFGShot'
        self.updateImageParameters()