from Thing.Thing import Thing
from doomConstants import *
from Vector.Vec2 import Vec
from doomUtils import get_class

class Monster( Thing ):

    def __init__(self):
        super(Monster, self).__init__()
        self.type = T_MONSTER
        self.hearRange = 256
        self.meleeRange = 64
        self.rangedRange = -1
        self.meleeDamage = 0.2
        self.lastAttacker = None
        self.attackerLastSeen = None
        self.player = None
        self.processingAI = True
        self.projectileType = None
        self.projectileSpeed = None
        self.accumulatedDelay = 0
        self.initialAttack = False
        self.attackDelay = 150

    def process_ai(self):
        if not self.processingAI:
            return
        if self.lastAttacker:
            pos = self.lastAttacker.getPosition()
            distance = pos - self.position
            distance = distance.getLength()
            if distance <= self.hearRange:
                self.attackerLastSeen = pos
                if distance <= self.meleeRange:
                    self.attackMelee( self.lastAttacker )
                    self.velocity = Vec2(0, 0)
                elif distance <= self.rangedRange:
                    self.attackRanged( self.lastAttacker )
                    self.velocity = Vec2(0, 0)
                else:
                    self.velocity = self.lastAttacker.getPosition() - self.position
                    self.velocity /= self.velocity.getLength()
            elif self.attackerLastSeen:
                self.velocity = self.attackerLastSeen - self.position
                self.velocity /= self.velocity.getLength()
        elif self.player:
            pos = self.player.getPosition()
            distance = pos - self.position
            dist = distance.getLength()
            if dist <= self.hearRange:
                self.velocity = distance
                self.lastAttacker = self.player
                self.attackerLastSeen = pos

    def attackMelee(self, thing):
        if self.accumulatedDelay < self.attackDelay:
            return
        thing.damage( self.meleeDamage )

    def attackRanged(self, thing):
        if self.accumulatedDelay < self attackDelay:
            return
        self.doomMap.addProjectile(get_class(self.projectileType)(self.position, (thing.getPosition() - self.position).normalize() * self.projectileSpeed, self.doomMap))
        #thing.damage( self.rangedDamage )

    def setPlayer(self, player):
        self.player = player

    def onDeath(self):
        super(Monster, self).onDeath()
        self.player.addKill()
        #self.image += '_dead'
