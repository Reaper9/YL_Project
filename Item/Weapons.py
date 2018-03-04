from doomConstants import *
from Thing.Thing import Thing


class Weapon(Thing):

    def __init__(self):
        super(Weapon, self).__init__()
        self.name = ''
        self.ammoType = None
        self.startingAmmo = 0
        self.type = T_ITEM
        self.pickup_message = ''
        self.display_time = 200
        self.shoot_sound = ''
        self.shoot_sound_path = ''

    def getType(self):
        return self.type

    def getWeaponType(self):
        return self.weaponType

    def getAmmoType(self):
        return self.ammoType

    def getStartingAmmo(self):
        return self.startingAmmo

    def onPickUp(self, thing):
        thing.giveWeapon(self)
        thing.addTextToDisplay(self.pickup_message, self.display_time)
        self.destroyed = True


class Fist(Weapon):

    def __init__(self):
        super(Fist, self).__init__()
        self.weaponType = W_FIST
        self.name = 'fist'


class Chainsaw(Weapon):

    def __init__(self):
        super(Chainsaw, self).__init__()
        self.weaponType = W_CHAINSAW
        self.name = 'chainsaw'
        self.pickup_message = 'chainsaw! find some meat'
        self.image = 'chainsaw'


class Pistol(Weapon):

    def __init__(self):
        super(Pistol, self).__init__()
        self.weaponType = W_PISTOL
        self.name = 'pistol'
        self.image = 'pistol'
        self.ammoType = A_BULLETS
        self.startingAmmo = 20
        self.pickup_message = 'picked up a pistol'
        self.shoot_sound = 'pistol_shot'
        self.shoot_sound_path = 'pistol_shot.ogg'


class Shotgun(Weapon):

    def __init__(self):
        super(Shotgun, self).__init__()
        self.weaponType = W_SHOTGUN
        self.name = 'shotgun'
        self.image = 'shotgun'
        self.ammoType = A_SHELLS
        self.startingAmmo = 20
        self.pickup_message = 'picked up a shotgun'
        self.shoot_sound = 'shotgun_shot'
        self.shoot_sound_path = 'shotgun_shot.ogg'


class SuperShotgun(Weapon):

    def __init__(self):
        super(SuperShotgun, self).__init__()
        self.weaponType = W_SUPERSHOTGUN
        self.name = 'super shotgun'
        self.image = 'super_shotgun'
        self.ammoType = A_SHELLS
        self.startingAmmo = 20
        self.pickup_message = 'picked up a super shotgun'
        self.shoot_sound = 'supershotgun_shot'
        self.shoot_sound_path = 'supershotgun_shot.ogg'


class Chaingun(Weapon):

    def __init__(self):
        super(Chaingun, self).__init__()
        self.weaponType = W_CHAINGUN
        self.name = 'chaingun'
        self.image = 'chaingun'
        self.ammoType = A_BULLETS
        self.startingAmmo = 50
        self.pickup_message = 'picked up a chaingun'
        self.shoot_sound = 'chaingun_shot'
        self.shoot_sound_path = 'chaingun_shot.ogg'


class RocketLauncher(Weapon):

    def __init__(self):
        super(RocketLauncher, self).__init__()
        self.weaponType = W_ROCKET_LAUNCHER
        self.name = 'rocket launcher'
        self.image = 'rocket_launcher'
        self.ammoType = A_ROCKETS
        self.startingAmmo = 10
        self.pickup_message = 'picked up a rocket launcher'
        self.shoot_sound = 'rocket_launcher_shot'
        self.shoot_sound_path = 'rocket_launcher_shot.ogg'


class PlasmaGun(Weapon):

    def __init__(self):
        super(PlasmaGun, self).__init__()
        self.weaponType = W_PLASMAGUN
        self.name = 'plasma gun'
        self.image = 'plasma_gun'
        self.ammoType = A_CELLS
        self.startingAmmo = 50
        self.pickup_message = 'picked up a plasma gun'
        self.shoot_sound = 'plasmagun_shot'
        self.shoot_sound_path = 'plasmagun_shot.ogg'


class BFG9000(Weapon):

    def __init__(self):
        super(BFG9000, self).__init__()
        self.weaponType = W_BFG9000
        self.name = 'BFG9000'
        self.image = 'BFG9000'
        self.ammoType = A_CELLS
        self.startingAmmo = 50
        self.pickup_message = 'picked up BFG9000! oh, yeah'
        self.shoot_sound = 'BFG9000_shot'
        self.shoot_sound_path = 'BFG9000_shot.ogg'
