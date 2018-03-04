from Thing.Thing import Thing
from Thing.DoomPlayer.doomPlayer import DoomPlayer
from doomConstants import *


class DoomCamera:

    def __init__(self):
        self.viewWidth = 10
        self.viewHeight = 5
        self.x = 0
        self.y = 0
        self.following = False
        self.thingFollowed = None
        self.center = [0, 0]

    def getViewWidth(self):
        return self.viewWidth

    def getViewHeight(self):
        return self.viewHeight

    def setViewWidth(self, width):
        self.viewWidth = width

    def setViewWidth(self, height):
        self.viewHeight = height

    def follow(self, thing):
        if type(thing) is Thing or type(thing) is DoomPlayer:
            self.thingFollowed = thing
            self.following = True

    def move(self, xMove, yMove):
        self.x += xMove
        self.y += yMove

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setCenter(self, center):
        self.center = center

    def getCenterX(self):
        return self.center[0]

    def getCenterY(self):
        return self.center[1]

    def getThingFollowed(self):
        return self.thingFollowed

    def updateMovement(self):
        if self.following:
            self.x = self.thingFollowed.getPosition().getX() - self.viewWidth * MAP_TILE_WIDTH // 2
            self.y = self.thingFollowed.getPosition().getY() - self.viewHeight * MAP_TILE_HEIGHT // 2
