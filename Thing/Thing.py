from Vector.Vec2 import Vec2
from doomClass import DoomClass
from doomConstants import *
from DoomMap.MapSpecial import *
from math import atan2, degrees


class Thing(DoomClass):

    def __init__(self, x=0, y=0):
        super(Thing, self).__init__()
        self.position = Vec2(x, y)
        self.velocity = Vec2(0, 0)
        self.image = None
        self.type = None
        self.doomMap = None
        self.imageWidth = None
        self.imageHeight = None
        self.rect = None
        self.x = 0
        self.y = 0
        self.health = 0
        self.meleeDamage = 0
        self.rangedDamage = 0
        self.processingAI = False
        self.dead = False
        self.angle = 0
        self.destroyed = False

    def updateMovement(self, deltaTime):
        expectedPosition = self.position + self.velocity * deltaTime
        if self.image == 'player':
            pass  # print(self.position)
            # print( expectedPosition.getX() / MAP_TILE_WIDTH, expectedPosition.getY() / MAP_TILE_HEIGHT )
        # if self.doomMap and not self.doomMap.getCollision( int( ( expectedPosition.getX() + ( self.imageWidth if self.velocity.getX() >= 0 else - self.imageWidth ) ) // MAP_TILE_WIDTH ), int( ( expectedPosition.getY() + ( self.imageHeight if self.velocity.getY() >= 0 else -self.imageHeight ) ) // MAP_TILE_HEIGHT ) ):
        #    self.position = expectedPosition
        if self.doomMap:
            x, y = int(expectedPosition.getX()) + self.imageWidth // 2, int(
                expectedPosition.getY()) + self.imageHeight // 2
            #x, y = int(expectedPosition.getX()), int(expectedPosition.getY())
            # if self.velocity.getX() > 0:
            #    x += self.imageWidth / 2
            # elif self.velocity.getX() < 0:
            #    x -= self.imageWidth / 2
            # if self.velocity.getY() > 0:
            #    x += self.imageHeight / 2
            # elif self.velocity.getY() < 0:
            #    x -= self.imageHeight / 2
            # x = round( x // MAP_TILE_WIDTH )
            # y = round( y // MAP_TILE_HEIGHT )
            self.x = x
            self.y = y
            # print(not self.doomMap.getCollision( ( x + self.imageWidth // 2 ) // MAP_TILE_WIDTH, y // MAP_TILE_HEIGHT ), not self.doomMap.getCollision( x // MAP_TILE_WIDTH, ( y + self.imageHeight // 2 ) // MAP_TILE_HEIGHT ), not self.doomMap.getCollision( ( x - self.imageWidth // 2 ) // MAP_TILE_WIDTH, y // MAP_TILE_HEIGHT ), not self.doomMap.getCollision( x // MAP_TILE_WIDTH, ( y - self.imageHeight // 2 ) // MAP_TILE_HEIGHT ))
            if not self.doomMap.getCollision((x + self.imageWidth // 2) // MAP_TILE_WIDTH,
                                             y // MAP_TILE_HEIGHT) and not self.doomMap.getCollision(
                    x // MAP_TILE_WIDTH,
                    (y + self.imageHeight // 2) // MAP_TILE_HEIGHT) and not self.doomMap.getCollision(
                    (x - self.imageWidth // 2) // MAP_TILE_WIDTH,
                    y // MAP_TILE_HEIGHT) and not self.doomMap.getCollision(x // MAP_TILE_WIDTH, (
                                                                                                         y - self.imageHeight // 2) // MAP_TILE_HEIGHT):
                self.position = expectedPosition
            self.processMapSpecials()
            # rct = pygame.Rect( x - MAP_TILE_WIDTH // 2, y - MAP_TILE_HEIGHT // 2, MAP_TILE_WIDTH, MAP_TILE_HEIGHT )
            # rct2 = pygame.Rect( self.position.getX() - self.imageWidth // 2, self.position.getY() - self.imageHeight // 2, self.imageWidth, self.imageHeight )
            # if self.doomMap and not self.doomMap.getCollision( x, y ) and not rct.colliderect( rct2 ) :
            #    self.position = expectedPosition
            # if not self.doomMap.getCollision( x, y ) and not self.doomMap.getCollision( int( expectedPosition.getX() // MAP_TILE_WIDTH ), int( expectedPosition.getY() // MAP_TILE_HEIGHT ) ):
            #    self.position = expectedPosition

    def initParameters(self):
        self.parameters = {T_IS_DRAWABLE: True}

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position = position

    def getImageName(self):
        return self.image

    def setType(self, type):
        self.type = type

    def getType(self):
        return self.type

    def updateImageParameters(self):
        self.imageWidth = self.doomMap.getThingImage(self.image).get_rect()[2]
        self.imageHeight = self.doomMap.getThingImage(self.image).get_rect()[3]
        self.rect = self.doomMap.getThingImage(self.image).get_rect()

    def updateImage(self):
        x = 0
        if self.velocity.getX() != 0:
            x = self.velocity.normalize().getX()
        if self.velocity.getY() != 0:
            y = self.velocity.normalize().getY()
        elif self.velocity.getX() != 0:
            y = 0
        else:
            y = -1
        self.angle = degrees(atan2(y, x)) + 90
        if self.angle < 0:
            self.angle += 360

    def setVelocity(self, velocity):
        self.velocity = velocity

    def getVelocity(self):
        return self.velocity

    def addVelocity(self, velocityAdd):
        self.velocity += velocityAdd

    def subVelocity(self, velocitySub):
        self.velocity -= velocitySub

    def setDoomMap(self, doomMap):
        self.doomMap = doomMap

    def getDoomMap(self):
        return self.doomMap

    def getImageWidth(self):
        return self.imageWidth

    def getImageHeight(self):
        return self.imageHeight

    def processMapSpecials(self):
        pass

    def validateConstant(self, constantName):
        return constantName in M_THING_CONSTANTS

    def damage(self, amount):
        pass

    def processHealth(self):
        pass

    def setCoords(self, x, y):
        self.position = Vec2(x, y)

    def getHealth(self):
        return self.health

    def setMeleeDamage(self, dmg):
        self.meleeDamage = dmg

    def getMeleeDamage(self):
        return self.meleeDamage

    def damage(self, amount):
        self.health -= amount
        self.processHealth()

    def processHealth(self):
        if self.health <= 0:
            self.onDeath()

    def onDeath(self):
        self.processingAI = False
        self.velocity = Vec2(0, 0)
        self.dead = True

    def process_ai(self):
        pass

    def setX(self, x):
        self.position.setX(x)

    def setY(self, y):
        self.position.setY(y)

    def isDead(self):
        return self.dead

    def setDead(self, dead):
        self.dead = dead

    def getAngle(self):
        return self.angle

    def getDestroyed(self):
        return self.destroyed