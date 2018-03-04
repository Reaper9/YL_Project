from Thing.Thing import Thing
from doomConstants import *
from Vector.Vec2 import Vec2
from Thing.Projectile import *
import pygame


class DoomPlayer(Thing):

    def __init__(self):
        self.ammo = {}
        self.weapons = {}
        super(DoomPlayer, self).__init__()
        self.image = 'marine_front'
        self.type = T_PLAYER
        self.health = 100
        self.armor = 0
        self.armorCoeff = 0
        self.secretsFound = 0
        self.mapKills = 0
        self.itemsFound = 0
        self.weaponSelected = W_FIST
        self.camera = None
        self.mapFinished = False
        self.nextMap = ''
        self.paused = False
        self.attack_coords = None
        self.attacking = False
        self.accumulatedDelay = 0
        self.initialShot = False
        self.textToDisplay = []
        self.sndSrv = None

    def updateMovement(self, deltaTime):
        super(DoomPlayer, self).updateMovement(deltaTime)
        for thing in self.doomMap.getThings():
            if thing.getType() == T_ITEM:
                tX, tY = int(thing.getPosition().getX() // MAP_TILE_WIDTH), (thing.getPosition().getY() // MAP_TILE_HEIGHT)
                if tX == int(self.getPosition().getX() // MAP_TILE_WIDTH) and tY == int(self.position.getY() // MAP_TILE_HEIGHT):
                    self.pickUp(thing)
        self.processPowerUps(deltaTime)
        self.processMapSpecials()
        if self.attacking:
            self.attack_coords = pygame.mouse.get_pos()
            self.attack_coords = [self.attack_coords[0], self.attack_coords[1]]
            self.accumulatedDelay += deltaTime
            self.attack(self.attack_coords)
        for text in self.textToDisplay:
            text[1] -= deltaTime
            if text[1] <= 0:
                self.textToDisplay.remove(text)

    def processMapSpecials(self):
        mapSpecials = self.doomMap.getMapSpecials(self.position.getX() // MAP_TILE_WIDTH, self.position.getY() // MAP_TILE_HEIGHT)
        if mapSpecials is not None:
            for mapSpecial in mapSpecials:
                if mapSpecial.getType() == MAP_SPECIAL_SECRET:
                    pass
                elif mapSpecial.getType() == MAP_SPECIAL_DAMAGING_FLOOR and not self.parameters[P_POWERUP_SUIT] and not \
                        self.parameters[P_POWERUP_INVULNERABILITY]:
                    mapSpecial.trigger(self)
                elif mapSpecial.getType() == MAP_SPECIAL_TELEPORT:
                    mapSpecial.trigger(self)
                elif mapSpecial.getType() == MAP_SPECIAL_EXIT_TILE:
                    self.mapFinished = True
                    mapSpecial.trigger(self)

    def damage(self, amount):
        if self.parameters[P_POWERUP_INVULNERABILITY]:
            amount = max(0, amount - 5000)
        amt = amount
        amt -= min(self.armor, amount) * self.armorCoeff
        self.armor = max(0, self.armor - amount * self.armorCoeff)
        self.health -= amount
        self.processHealth()
        self.sndSrv.startSound(P_PAIN)

    def initParameters(self):
        super(DoomPlayer, self).initParameters()
        self.parameters[P_POWERUP_BERSERK] = False
        self.parameters[P_POWERUP_INVISIBILITY] = False
        self.parameters[P_POWERUP_INVULNERABILITY] = False
        self.parameters[P_POWERUP_MAP] = False
        self.parameters[P_POWERUP_SUIT] = False
        self.parameters[A_BULLETS] = A_BULLETS_MAX
        self.parameters[A_SHELLS] = A_SHELLS_MAX
        self.parameters[A_ROCKETS] = A_ROCKETS_MAX
        self.parameters[A_CELLS] = A_CELLS_MAX
        self.ammo[A_BULLETS] = 50
        self.ammo[A_SHELLS] = 0
        self.ammo[A_ROCKETS] = 0
        self.ammo[A_CELLS] = 0
        self.weapons[W_FIST] = True
        self.weapons[W_PISTOL] = True
        self.health = 100
        self.armor = 0
        self.armorCoeff = 0
        self.dead = False
        self.paused = False
        self.position = Vec2(-10000, -10000)
        self.velocity = Vec2(0, 0)

    def pickUp(self, item):
        item.onPickUp(self)

    def attack(self, crds):
        if self.initialShot:
            self.accumulatedDelay = W_MAX_DELAY
        coords = [0, 0]
        coords[0] = crds[0] + self.camera.getX()
        coords[1] = crds[1] + self.camera.getY()
        if self.weaponSelected == W_FIST and self.accumulatedDelay >= W_FIST_DELAY:
            if (self.position - Vec2(coords[0], coords[1])).getLength() <= W_FIST_RANGE:
                self.shoot(coords, W_FIST_DAMAGE)
        elif self.weaponSelected == W_CHAINSAW and self.accumulatedDelay >= W_CHAINSAW_DELAY:
            if (self.position - Vec2(coords[0], coords[1])).getLength() <= W_CHAINSAW_RANGE:
                self.shoot(coords, W_CHAINSAW_DAMAGE)
        elif self.weaponSelected == W_PISTOL and self.ammo[A_BULLETS] >= W_PISTOL_AMMO_PER_SHOT and self.accumulatedDelay >= W_PISTOL_DELAY:
            self.shoot(coords, W_PISTOL_DAMAGE, PROJ_BULLET_SPEED, Bullet)
            self.takeAmmo(A_BULLETS, W_PISTOL_AMMO_PER_SHOT)
            self.sndSrv.startSound(W_PISTOL_SHOT)
        elif self.weaponSelected == W_SHOTGUN and self.ammo[A_SHELLS] >= W_SHOTGUN_AMMO_PER_SHOT and self.accumulatedDelay >= W_SHOTGUN_DELAY:
            self.shoot(coords, W_SHOTGUN_DAMAGE, PROJ_SHELL_SPEED, Shell)
            self.takeAmmo(A_SHELLS, W_SHOTGUN_AMMO_PER_SHOT)
            self.sndSrv.startSound(W_SHOTGUN_SHOT)
        elif self.weaponSelected == W_SUPERSHOTGUN and self.ammo[A_SHELLS] >= W_SUPERSHOTGUN_AMMO_PER_SHOT and self.accumulatedDelay >= W_SUPERSHOTGUN_DELAY:
            self.shoot(coords, W_SUPERSHOTGUN_DAMAGE, PROJ_SHELL_SPEED, Shell)
            self.takeAmmo(A_SHELLS, W_SUPERSHOTGUN_AMMO_PER_SHOT)
            self.sndSrv.startSound(W_SUPERSHOTGUN_SHOT)
        elif self.weaponSelected == W_CHAINGUN and self.ammo[A_BULLETS] >= W_CHAINGUN_AMMO_PER_SHOT and self.accumulatedDelay >= W_CHAINSAW_DELAY:
            self.shoot(coords, W_CHAINGUN_DAMAGE, PROJ_BULLET_SPEED, Bullet)
            self.takeAmmo(A_BULLETS, W_CHAINGUN_AMMO_PER_SHOT)
            self.sndSrv.startSound(W_PISTOL_SHOT)
        elif self.weaponSelected == W_ROCKET_LAUNCHER and self.ammo[A_ROCKETS] >= W_ROCKET_LAUNCHER_AMMO_PER_SHOT and self.accumulatedDelay >= W_ROCKET_LAUNCHER_DELAY:
            self.shoot(coords, W_ROCKET_LAUNCHER_DAMAGE, PROJ_ROCKET_SPEED, Rocket)
            self.takeAmmo(A_ROCKETS, W_ROCKET_LAUNCHER_AMMO_PER_SHOT)
            self.sndSrv.startSound(W_ROCKET_LAUNCHER_SHOT)
        elif self.weaponSelected == W_PLASMAGUN and self.ammo[A_CELLS] >= W_PLASMAGUN_AMMO_PER_SHOT and self.accumulatedDelay >= W_PLASMAGUN_DELAY:
            self.shoot(coords, W_PLASMAGUN_DAMAGE, PROJ_PLASMA_SPEED, Plasma)
            self.takeAmmo(A_CELLS, W_PLASMAGUN_AMMO_PER_SHOT)
            self.sndSrv.startSound(W_PLASMAGUN_SHOT)
        elif self.weaponSelected == W_BFG9000 and self.ammo[A_CELLS] >= W_BFG9000_AMMO_PER_SHOT and self.accumulatedDelay >= W_BFG9000_DELAY:
            self.shoot(coords, W_BFG9000_DAMAGE, PROJ_BFG_SPEED, BFGProjectile)
            self.takeAmmo(A_CELLS, W_BFG9000_AMMO_PER_SHOT)
            self.sndSrv.startSound(W_BFG9000_SHOT)

    def shoot(self, coords, damage, projectileSpeed, projectileType):
        self.accumulatedDelay = 0
        self.initialShot = False
        self.doomMap.addProjectile(projectileType(self.position, (Vec2(coords[0], coords[1]) - self.position).normalize() * projectileSpeed, damage, self.doomMap))
        #for thing in self.doomMap.getThings():
        #    if thing.getType() == T_MONSTER:
        #        tX, tY = int(thing.getPosition().getX() // MAP_TILE_WIDTH), (thing.getPosition().getY() // MAP_TILE_HEIGHT)
        #        if tX == coords[0] // MAP_TILE_WIDTH and tY == coords[1] // MAP_TILE_HEIGHT:
        #            thing.damage(damage)

    def getArmor(self):
        return self.armor

    def getArmorCoeff(self):
        return self.armorCoeff

    def setArmor(self, armor):
        self.armor = armor

    def setArmorCoeff(self, armorCoeff):
        self.armorCoeff = armorCoeff

    def processPowerUps(self, deltaTime):
        for parameter in (P_POWERUP_INVULNERABILITY, P_POWERUP_INVISIBILITY, P_POWERUP_SUIT):
            if self.parameters[parameter] != False:
                self.parameters[parameter] -= deltaTime
                if self.parameters[parameter] <= 0:
                    self.parameters[parameter] = False

    def onDeath(self):
        super(DoomPlayer, self).onDeath()
        self.paused = True
        self.dead = True
        self.sndSrv.startSound(P_DEATH)

    def process_ai(self):
        pass

    def giveWeapon(self, weapon):
        self.weapons[weapon.getWeaponType()] = True
        if weapon.getAmmoType() is not None:
            self.giveAmmo(weapon.getAmmoType(), weapon.getStartingAmmo())

    def giveAmmo(self, ammoType, ammo):
        self.ammo[ammoType] = min(self.ammo.get(ammoType, 0) + ammo, self.parameters.get(ammoType))

    def takeAmmo(self, ammoType, amount):
        self.ammo[ammoType] = max(0, self.ammo[ammoType] - amount)

    def setCamera(self, camera):
        self.camera = camera

    def addKill(self):
        self.mapKills += 1

    def isMapFinished(self):
        return self.mapFinished

    def setNextMap(self, nextMap):
        self.nextMap = nextMap

    def setMapFinished(self, mapFinished):
        self.mapFinished = mapFinished

    def setDoomMap(self, doomMap):
        super(DoomPlayer, self).setDoomMap(doomMap)
        self.position = Vec2(doomMap.getStartX(), doomMap.getStartY())

    def getNextMap(self):
        return self.nextMap

    def getPaused(self):
        return self.paused

    def setPaused(self, paused):
        self.paused = paused

    def updateImage(self):
        super(DoomPlayer, self).updateImage()
        if self.velocity.getX() == 0 and self.velocity.getY() == 0:
            self.image = 'marine_front'
        elif self.angle <= 22.5 or self.angle >= 342.5:
            self.image = 'marine_back'
        elif 22.5 < self.angle <= 67.5:
            self.image= 'marine_back_right'
        elif 67.5 < self.angle <= 112.5:
            self.image = 'marine_right'
        elif 112.5 < self.angle <= 157.5:
            self.image = 'marine_front_right'
        elif 157.5 < self.angle <= 202.5:
            self.image = 'marine_front'
        elif 202.5 < self.angle <= 247.5:
            self.image = 'marine_front_left'
        elif 247.5 < self.angle <= 292.5:
            self.image = 'marine_left'
        else:
            self.image = 'marine_back_left'
        self.angle = 0
        self.updateImageParameters()

    def selectWeapon(self, weapon):
        if weapon == W_FIST and self.weaponSelected == W_FIST:
            weapon = W_CHAINSAW
        elif weapon == W_SHOTGUN and self.weaponSelected == W_SHOTGUN:
            weapon = W_SUPERSHOTGUN
        if weapon in self.weapons.keys():
            self.weaponSelected = weapon

    def getCurrentAmmo(self):
        if self.weaponSelected == W_FIST or self.weaponSelected == W_CHAINSAW:
            return 0
        elif self.weaponSelected == W_SHOTGUN or self.weaponSelected == W_SUPERSHOTGUN:
            return self.ammo[A_SHELLS]
        elif self.weaponSelected == W_PISTOL or self.weaponSelected == W_CHAINGUN:
            return self.ammo[A_BULLETS]
        elif self.weaponSelected == W_ROCKET_LAUNCHER:
            return self.ammo[A_ROCKETS]
        elif self.weaponSelected == W_PLASMAGUN or self.weaponSelected == W_BFG9000:
            return self.ammo[A_CELLS]

    def hasWeapon(self, weapon):
        return self.weapons.get(weapon, False)

    def getAmmo(self, ammoType):
        return self.ammo.get(ammoType, 0)

    def getMaxAmmo(self, ammoType):
        return self.parameters[ammoType]

    def startAttacking(self, crds):
        self.attack_coords = crds
        self.attacking = True
        self.initialShot = True

    def stop_attacking(self):
        self.attacking = False
        self.accumulatedDelay = 0

    def setParameter(self, parameterName, newVal):
        self.parameters[parameterName] = newVal

    def getTextToDisplay(self):
        return self.textToDisplay

    def addTextToDisplay(self, text, time):
        self.textToDisplay.append([text, time])

    def setSndSrv(self, sndSrv):
        self.sndSrv = sndSrv