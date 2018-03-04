from copy import deepcopy
from Thing.Thing import Thing
from Thing.DoomPlayer.doomPlayer import DoomPlayer
import pygame
import os
from Thing.Monster.Monster import Monster
from SndSrv import SndSrv


class DoomMap:
    def __init__(self, width, height):
        self.title = ''
        self.width = width
        self.height = height
        self.mapData = []
        self.thingsData = []
        self.tileImages = []
        self.thingsImages = {}
        self.collisionData = []
        self.mapSpecials = {}
        self.projectiles = []
        self.name = ''
        self.startX = 0
        self.startY = 0
        self.mapMusic = ''
        self.isEndMap = False
        self.sndSrv = None

    def getTile(self, x, y):
        if x < self.width and y < self.height:
            return self.mapData[x][y]
        else:
            pass

    def setTile(self, x, y, tile):
        pass

    def setWidth(self, width):
        if width > 0:
            self.width = width
        else:
            pass

    def setHeight(self, height):
        if height > 0:
            self.height = height
        else:
            pass

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def addThing(self, thing):
        if type(thing) is Thing or type(thing) is DoomPlayer or type(thing) is Monster:
            self.thingsData.append(thing)
        else:
            pass

    def addProjectile(self, projectile):
        self.projectiles.append(projectile)

    def removeProjectile(self, projectile):
        self.projectiles.remove(projectile)

    def removeThing(self, thing):
        if thing in self.thingsData:
            self.thingsData.remove(thing)
        else:
            pass

    def getTileImage(self, tile):
        return self.tileImages[tile]

    def getRow(self, row):
        return self.mapData[row]

    def getThings(self):
        return self.thingsData

    def getThingImage(self, thingName):
        return self.thingsImages[thingName]

    def getCollision(self, x, y):
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return True
        return self.collisionData[y][x]

    def loadMapData(self, newMapData):
        self.name = newMapData[0]
        self.width = newMapData[1]
        self.height = newMapData[2]
        self.startX = newMapData[3]
        self.startY = newMapData[4]
        self.mapMusic = newMapData[5]
        self.isEndMap = newMapData[6]
        self.mapData = deepcopy(newMapData[7])
        #self.sndSrv.load_music(self.mapMusic)
        #self.sndSrv.start_music(-1)

    def loadCollisionData(self, newCollisionData):
        self.collisionData = deepcopy(newCollisionData[2])

    def loadThingsData(self, newThingsData):
        self.thingsData = newThingsData

    def loadTileImages(self, tileImagePaths):
        for path in tileImagePaths:
            self.tileImages.append(pygame.image.load(os.path.join('base', path)))

    def loadThingsImages(self, thingsImagePaths):
        for pair in thingsImagePaths.items():
            self.thingsImages[pair[0]] = pygame.image.load(os.path.join('base', pair[1]))

    def loadMapSpecials(self, mapSpecials):
        self.mapSpecials = mapSpecials

    def getMapSpecials(self, x, y):
        return self.mapSpecials.get((x, y), None)

    def getStartX(self):
        return self.startX

    def getStartY(self):
        return self.startY

    def processProjectiles(self, deltaTime):
        for projectile in self.projectiles:
            if projectile.isDestroyed():
                self.projectiles.remove(projectile)
                del projectile
            else:
                projectile.updateMovement(deltaTime, self.thingsData)

    def getProjectiles(self):
        return self.projectiles

    def processThings(self):
        for thing in self.thingsData:
            if thing.getDestroyed():
                self.thingsData.remove(thing)
                del thing

    def isEnding(self):
        return self.isEndMap

    def setSndSrv(self, sndSrv):
        self.sndSrv = sndSrv