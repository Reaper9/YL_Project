from doomConstants import *
from Thing.Thing import Thing


class PowerUp(Thing):

    def __init__(self):
        super(PowerUp, self).__init__()
        self.powerUpType = None
        self.time = 0
        self.type = T_ITEM
        self.pickup_message = ''
        self.display_time = 200

    def onPickUp(self, thing):
        thing.addTextToDisplay(self.pickup_message, self.display_time)
        self.destroyed = True


class HealthPickup(PowerUp):

    def __init__(self):
        super(HealthPickup, self).__init__()
        self.healAmount = 0
        self.healThreshold = 0

    def onPickUp(self, thing):
        super(HealthPickup, self).onPickUp(thing)
        if thing.getHealth() < self.healThreshold:
            thing.damage(-min(self.healThreshold - thing.getHealth(), self.healAmount))


class healthVial(HealthPickup):

    def __init__(self):
        super(healthVial, self).__init__()
        self.healAmount = 2
        self.healThreshold = 200
        self.powerUpType = I_HEALTH_VIAL
        self.pickup_message = 'picked up a health bonus'
        self.image = 'health_bonus'


class Stimpack(HealthPickup):

    def __init__(self):
        super(Stimpack, self).__init__()
        self.healAmount = 25
        self.healThreshold = 100
        self.powerUpType = I_STIMPACK
        self.pickup_message = 'picked up a stimpack'
        self.image = 'stimpack'


class Medikit(HealthPickup):

    def __init__(self):
        super(Medikit, self).__init__()
        self.healAmount = 50
        self.healThreshold = 100
        self.powerUpType = I_MEDIKIT
        self.pickup_message = 'picked up a medikit'
        self.image = 'medikit'


class Soulsphere(HealthPickup):

    def __init__(self):
        super(Soulsphere, self).__init__()
        self.healAmount = 100
        self.healThreshold = 200
        self.powerUpType = I_SOULSPHERE
        self.pickup_message = 'supercharge!'
        self.image = 'soulsphere'


class Armor(PowerUp):

    def __init__(self):
        super(Armor, self).__init__()
        self.armorAmount = 0
        self.armorCoeff = 0
        self.armorThreshold = 0

    def onPickUp(self, thing):
        super(Armor, self).onPickUp(thing)
        if thing.getArmor() < self.armorThreshold:
            thing.setArmor(min(self.armorThreshold - thing.getArmor(), self.armorAmount))
            thing.setArmorCoeff(max(thing.getArmorCoeff(), self.armorCoeff))


class ArmorShard(Armor):

    def __init__(self):
        super(ArmorShard, self).__init__()
        self.armorAmount = 5
        self.armorThreshold = 200
        self.armorCoeff = 0.33
        self.powerUpType = I_ARMOR_SHARD
        self.pickup_message = 'picked up an armor bonus'
        self.image = 'armor_bonus'


class ArmorGreen(Armor):

    def __init__(self):
        super(ArmorGreen, self).__init__()
        self.armorAmount = 100
        self.armorThreshold = 100
        self.armorCoeff = 0.33
        self.powerUpType = I_ARMOR_GREEN
        self.pickup_message = 'you\'ve got a security armor!'
        self.image = 'armor_green'


class ArmorBlue(Armor):

    def __init__(self):
        super(ArmorBlue, self).__init__()
        self.armorAmount = 200
        self.armorThreshold = 200
        self.armorCoeff = 0.66
        self.powerUpType = I_ARMOR_BLUE
        self.pickup_message = 'you\'ve got a combat armor!'
        self.image = 'armor_blue'


class Berserk(PowerUp):

    def __init__(self):
        super(Berserk, self).__init__()
        self.newDamage = 40
        self.powerUpType = I_BERSERK
        self.pickup_message = 'berserk!'
        self.image = 'berserk'

    def onPickUp(self, thing):
        super(Berserk, self).onPickUp(thing)
        thing.setParameter(P_POWERUP_BERSERK, True)
        thing.setMeleeDamage(max(thing.getMeleeDamage(), self.newDamage))


class Invulnerability(PowerUp):

    def __init__(self):
        super(Invulnerability, self).__init__()
        self.time = 250
        self.powerUpType = I_INVULNERABILITY
        self.pickup_message = 'invulnerability!'
        self.image = 'invulnerability'

    def onPickUp(self, thing):
        super(Invulnerability, self).onPickUp(thing)
        thing.setParameter(P_POWERUP_INVULNERABILITY, self.time)


class Invisibility(PowerUp):

    def __init__(self):
        super(Invisibility, self).__init__()
        self.time = 250
        self.powerUpType = I_INVISIBILITY
        self.pickup_message = 'invisibility!'
        self.image = 'invisibility'

    def onPickUp(self, thing):
        super(Invisibility, self).onPickUp(thing)
        thing.setParameter(P_POWERUP_INVISIBILITY, self.time)


class AreaMap(PowerUp):

    def __init__(self):
        super(AreaMap, self).__init__()
        self.powerUpType = I_AREA_MAP
        self.pickup_message = 'area map!'
        self.image = 'area_map'

    def onPickUp(self, thing):
        super(AreaMap, self).onPickUp(thing)
        thing.setParameter(P_POWERUP_MAP, True)


class Suit(PowerUp):

    def __init__(self):
        super(Suit, self).__init__()
        self.powerUpType = I_SUIT
        self.time = 6000
        self.pickup_message = 'radiation suit!'
        self.image = 'rad_suit'

    def onPickUp(self, thing):
        super(Suit, self).onPickUp(thing)
        thing.setParameter(P_POWERUP_SUIT, self.time)
