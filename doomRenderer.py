from doomConstants import *
from doomClass import DoomClass
from DoomCamera import DoomCamera
import pygame


class DoomRenderer(DoomClass):

    def __init__(self):
        super(DoomRenderer, self).__init__()
        self.doomMap = None
        self.camera = None
        self.surface = None
        self.pointerImg = pygame.image.load('base\\pointer.png')
        self.gui = None
        self.viewWidth = 0
        self.viewHeight = 0

    def render(self):
        if self.parameters[G_DRAW_TILES]:
            mapWidth = self.doomMap.getWidth()
            mapHeight = self.doomMap.getHeight()
            for row in range(mapHeight):
                mapRow = self.doomMap.getRow(row)
                for tile in range(mapWidth):
                    self.surface.blit(self.doomMap.getTileImage(mapRow[tile]), (
                    tile * MAP_TILE_WIDTH - self.camera.getX() - MAP_TILE_WIDTH // 2,
                    row * MAP_TILE_HEIGHT - self.camera.getY() - MAP_TILE_HEIGHT // 2))
                    # self.surface.blit( self.doomMap.getTileImage( mapRow[tile] ), ( ( tile * MAP_TILE_WIDTH - self.camera.getX() ) + self.camera.getViewWidth() // 2 * MAP_TILE_WIDTH, ( row * MAP_TILE_HEIGHT - self.camera.getY() ) + self.camera.getViewHeight() // 2 * MAP_TILE_HEIGHT ) )
            # print(range( max( self.camera.getY() // MAP_TILE_HEIGHT - self.camera.getViewHeight() // 2, 0 ), min( mapHeight, self.camera.getY() // MAP_TILE_HEIGHT + self.camera.getViewHeight() // 2 )))
            # for row in range( max( self.camera.getY()// MAP_TILE_HEIGHT - self.camera.getViewHeight() // 2, 0 ), min( mapHeight, self.camera.getY() + self.camera.getViewHeight() // 2 ) ):
            #    mapRow = self.doomMap.getRow( row )
            #    for tile in range( max( self.camera.getX() // MAP_TILE_WIDTH - self.camera.getViewWidth() // 2, 0), min( mapWidth, self.camera.getX() + self.camera.getViewWidth() // 2 ) ):
            #        self.surface.blit( self.doomMap.getTileImage( mapRow[tile] ), ( tile * MAP_TILE_WIDTH, row * MAP_TILE_HEIGHT ) )
        if self.parameters[G_DRAW_THINGS]:
            things = self.doomMap.getThings()
            if self.parameters[G_DRAW_ITEMS]:
                for thing in things:
                    if thing.getParameter(T_IS_DRAWABLE) and thing.getType() == T_ITEM:
                        pos = thing.getPosition()
                        self.surface.blit(self.doomMap.getThingImage(thing.getImageName()), (
                        pos.getX() - self.camera.getX() - thing.getImageWidth() // 2,
                        pos.getY() - self.camera.getY() - thing.getImageHeight() // 2))
            if self.parameters[G_DRAW_MONSTERS]:
                for thing in things:
                    if thing.getParameter(T_IS_DRAWABLE) and thing.getType() in (T_MONSTER, T_PLAYER):
                        pos = thing.getPosition()
                        self.surface.blit(pygame.transform.rotate(self.doomMap.getThingImage(thing.getImageName()), thing.getAngle()), (
                        pos.getX() - self.camera.getX() - thing.getImageWidth() // 2,
                        pos.getY() - self.camera.getY() - thing.getImageHeight() // 2))
        for projectile in self.doomMap.getProjectiles():
            pos = projectile.getPosition()
            self.surface.blit(pygame.transform.rotate(self.doomMap.getThingImage(projectile.getImageName()), projectile.getAngle()), (
                pos.getX() - self.camera.getX() - projectile.getImageWidth() // 2,
                pos.getY() - self.camera.getY() - projectile.getImageHeight() // 2))
        self.renderGUI()

    def renderGUI(self):
        if self.gui.getScreen() == S_GAME or self.gui.getScreen() == S_PAUSED:
            self.surface.blit(pygame.transform.scale(self.doomMap.getThingImage('hud'), (self.viewWidth, int(HUD_HEIGHT * (self.viewWidth / HUD_WIDTH)))), (0, self.viewHeight - HUD_HEIGHT * (self.viewWidth // HUD_WIDTH)))
        self.gui.render(self.surface)

    def validateConstant(self, constantName):
        if constantName in M_RENDER_CONSTANTS:
            return True
        else:
            pass

    def initParameters(self):
        self.parameters = {G_DRAW_ITEMS: True, G_DRAW_INVISIBLE: False, G_DRAW_MONSTERS: True, G_DRAW_TILES: True,
                           G_DRAW_THINGS: True}

    def setMap(self, doomMap):
        self.doomMap = doomMap

    def setCamera(self, camera):
        self.camera = camera

    def setSurface(self, surface):
        self.surface = surface

    def setViewWidth(self, viewWidth):
        self.viewWidth = viewWidth

    def setViewHeight(self, viewHeight):
        self.viewHeight = viewHeight

    def setGUI(self, gui):
        self.gui = gui
