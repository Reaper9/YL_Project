from Thing.Thing import Thing
from doomConstants import *


class DoomInventory:

    def __init__(self, initialItems=[]):
        self.items = initialItems

    def addItem(self, item):
        if type(item) is Thing:
            self.items.append(item)
            item.setParameter(T_IS_DRAWABLE, False)
        else:
            pass

    def removeItem(self, item):
        if item in self.items:
            self.items.remove(item)
            item.setParameter(T_IS_DRAWABLE, True)
        else:
            pass

    def getItems(self):
        return self.items

    def __contains__(self, item):
        return item in self.items
