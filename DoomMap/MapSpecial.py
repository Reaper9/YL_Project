from doomClass import DoomClass
from doomConstants import *


class MapSpecial(DoomClass):

    def __init__(self):
        super(MapSpecial, self).__init__()
        self.type = None

    def trigger(self, thing):
        pass

    def setType(self, type):
        self.type = type

    def getType(self):
        return self.type


class SecretSpecial(MapSpecial):

    def __init__(self):
        super(SecretSpecial, self).__init__()
        self.type = MAP_SPECIAL_SECRET
        self.revealMessage = 'A SECRET IS REVEALED'
        self.revealed = False
        self.id = None

    def trigger(self, thing):
        pass

    def setID(self, id):
        self.id = id


class TeleportSpecial(MapSpecial):

    def __init__(self):
        super(TeleportSpecial, self).__init__()
        self.type = MAP_SPECIAL_TELEPORT
        self.destX = None
        self.destY = None

    def trigger(self, thing):
        thing.setX(self.destX)
        thing.setY(self.destY)

    def setDestination(self, destX, destY):
        self.destX = destX
        self.destY = destY

    def setDestX(self, destX):
        self.destX = destX

    def setDestY(self, destY):
        self.destY = destY


class SwitchSpecial(MapSpecial):

    def __init__(self):
        super(SwitchSpecial, self).__init__()
        self.type = MAP_SPECIAL_SWITCH

    def trigger(self, thing):
        pass


class DamagingFloorSpecial(MapSpecial):

    def __init__(self):
        super(DamagingFloorSpecial, self).__init__()
        self.type = MAP_SPECIAL_DAMAGING_FLOOR
        self.damagePerTic = 0

    def trigger(self, thing):
        thing.damage(self.damagePerTic)

    def setDamage(self, damage):
        self.damagePerTic = damage


class ExitSwitch(MapSpecial):

    def __init__(self):
        super(ExitSwitch, self).__init__()
        self.type = MAP_SPECIAL_EXIT_SWITCH
        self.destinationMap = ''

    def trigger(self, thing):
        thing.setMapFinished(True)
        thing.setNextMap(self.destinationMap)

    def setDestinationMap(self, destMap):
        self.destinationMap = destMap


class ExitTile(MapSpecial):

    def __init__(self):
        super(ExitTile, self).__init__()
        self.type = MAP_SPECIAL_EXIT_TILE
        self.destinationMap = ''

    def trigger(self, thing):
        thing.setMapFinished(True)
        thing.setNextMap(self.destinationMap)

    def setDestinationMap(self, destMap):
        self.destinationMap = destMap
