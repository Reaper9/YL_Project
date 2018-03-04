from doomConstants import *
from Thing.Thing import Thing


class Ammo(Thing):

    def __init__(self):
        super(Ammo, self).__init__()
        self.ammoType = None
        self.amount = 0
        self.type = T_ITEM
        self.pickup_message = ''
        self.display_time = 200

    def getAmmoType(self):
        return self.ammoType

    def getType(self):
        return self.type

    def getAmount(self):
        return self.amount

    def onPickUp(self, thing):
        thing.giveAmmo(self.ammoType, self.amount)
        thing.addTextToDisplay(self.pickup_message, self.display_time)
        self.destroyed = True


class AmmoClip(Ammo):

    def __init__(self):
        super(AmmoClip, self).__init__()
        self.ammoType = A_BULLETS
        self.amount = 10
        self.image = 'ammo_clip'
        self.pickup_message = 'picked up an ammo clip'


class AmmoBox(Ammo):

    def __init__(self):
        super(AmmoBox, self).__init__()
        self.ammoType = A_BULLETS
        self.amount = 50
        self.image = 'ammo_box'
        self.pickup_message = 'picked up a box of bullets'


class ShellsFour(Ammo):

    def __init__(self):
        super(ShellsFour, self).__init__()
        self.ammoType = A_SHELLS
        self.amount = 4
        self.image = 'shells_four'
        self.pickup_message = 'picked up four shotgun shells'


class ShellsBox(Ammo):

    def __init__(self):
        super(ShellsBox, self).__init__()
        self.ammoType = A_SHELLS
        self.amount = 20
        self.image = 'shells_box'
        self.pickup_message = 'picked up a box of shotgun shells'


class RocketAmmo(Ammo):

    def __init__(self):
        super(RocketAmmo, self).__init__()
        self.ammoType = A_ROCKETS
        self.amount = 1
        self.image = 'rocket'
        self.pickup_message = 'picked up a rocket'


class RocketBox(Ammo):

    def __init__(self):
        super(RocketBox, self).__init__()
        self.ammoType = A_ROCKETS
        self.amount = 10
        self.image = 'rockets_box'
        self.pickup_message = 'picked up a box of rockets'


class EnergyCell(Ammo):

    def __init__(self):
        super(EnergyCell, self).__init__()
        self.ammoType = A_CELLS
        self.amount = 40
        self.image = 'energy_cell'
        self.pickup_message = 'picked up an energy cell'


class EnergyCellPack(Ammo):

    def __init__(self):
        super(EnergyCellPack, self).__init__()
        self.ammoType = A_CELLS
        self.amount = 200
        self.image = 'energy_cell_pack'
        self.pickup_message = 'picked up an energy cell pack'


class Backpack(Ammo):

    def __init__(self):
        pass
