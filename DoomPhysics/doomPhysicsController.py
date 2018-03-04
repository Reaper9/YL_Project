from doomClass import DoomClass
from Thing.Thing import Thing
from Thing.DoomPlayer.doomPlayer import DoomPlayer
from Thing.Monster.Monster import Monster


class DoomPhysicsController(DoomClass):

    def __init__(self):
        super(DoomPhysicsController, self).__init__()
        self.things = []

    def updateMovement(self, deltaTime):
        for thing in self.things:
            thing.updateMovement(deltaTime)
            thing.process_ai()
            thing.updateImage()
            if thing.getDestroyed():
                self.things.remove(thing)
                del thing

    def addThing(self, thing):
        if type(thing) is Thing or type(thing) is DoomPlayer or type(thing) is Monster:
            self.things.append(thing)
        else:
            pass

    def removeThing(self, thing):
        if thing in self.things:
            self.things.remove(thing)
        else:
            pass

    def addThings(self, things):
        self.things += things

    def setThings(self, things):
        self.things = things
