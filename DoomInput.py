from doomClass import DoomClass
from doomConstants import *
from Thing.DoomPlayer.doomPlayer import DoomPlayer
from Vector.Vec2 import Vec2
import pygame


class DoomInputController(DoomClass):

    def __init__(self):
        super(DoomInputController, self).__init__()
        self.player = None
        self.gui = None

    def processInput(self, event):
        if event.type == pygame.QUIT:
            return True
        elif self.gui.get_event(event):
            return False
        elif self.gui.getScreen() != S_GAME:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == C_MOVE_NORTH:
                self.player.addVelocity(Vec2(0, -P_MAX_SPEED))
            elif event.key == C_MOVE_SOUTH:
                self.player.addVelocity(Vec2(0, P_MAX_SPEED))
            elif event.key == C_MOVE_WEST:
                self.player.addVelocity(Vec2(-P_MAX_SPEED, 0))
            elif event.key == C_MOVE_EAST:
                self.player.addVelocity(Vec2(P_MAX_SPEED, 0))
        elif event.type == pygame.KEYUP:
            if event.key == C_MOVE_NORTH:
                self.player.subVelocity(Vec2(0, -P_MAX_SPEED))
            elif event.key == C_MOVE_SOUTH:
                self.player.subVelocity(Vec2(0, P_MAX_SPEED))
            elif event.key == C_MOVE_WEST:
                self.player.subVelocity(Vec2(-P_MAX_SPEED, 0))
            elif event.key == C_MOVE_EAST:
                self.player.subVelocity(Vec2(P_MAX_SPEED, 0))
            elif event.key == C_PAUSE:
                self.player.setPaused(True)
            elif event.key == C_FIST:
                self.player.selectWeapon(W_FIST)
            elif event.key == C_PISTOL:
                self.player.selectWeapon(W_PISTOL)
            elif event.key == C_SHOTGUN:
                self.player.selectWeapon(W_SHOTGUN)
            elif event.key == C_CHAINGUN:
                self.player.selectWeapon(W_CHAINGUN)
            elif event.key == C_ROCKET_LAUNCHER:
                self.player.selectWeapon(W_ROCKET_LAUNCHER)
            elif event.key == C_PLASMAGUN:
                self.player.selectWeapon(W_PLASMAGUN)
            elif event.key == C_BFG9000:
                self.player.selectWeapon(W_BFG9000)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.player.startAttacking(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.player.stop_attacking()
        return False

    def setPlayer(self, player):
        self.player = player

    def setGUI(self, gui):
        self.gui = gui
