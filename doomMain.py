from doomRenderer import DoomRenderer
from DoomPhysics.doomPhysicsController import DoomPhysicsController
from DoomInput import DoomInputController
from DoomIO.DoomMapLoader import DoomMapLoader
from DoomCamera import DoomCamera
from Thing.DoomPlayer.doomPlayer import DoomPlayer
from doomConstants import *
from doomMap import DoomMap
from Thing.Monster.Monster import Monster
from UI.UI import *
import pygame
from time import time
from SndSrv import SndSrv

windowSize, windowWidth, windowHeight, surface = None, None, None, None
doomMap = None
renderer = None
clock, deltaTime = None, None
exiting, running = None, None
physicsController = None
inputController = None
mapLoader = None
camera = None
player = None
sndSrv = None

mainMenu = []
episodeChoice = []
difficultyChoice = []
exitChoice = []
intermission = []
win = []
lose = []
gui = None
gameUI = []
pauseScreen = []

currentFrameMillis = 0
previousFrameMillis = 0

def doomInit():
    global windowSize, windowWidth, windowHeight, surface
    global doomMap
    global renderer
    global clock, deltaTime
    global exiting, running
    global physicsController
    global inputController
    global mapLoader
    global camera
    global player
    global gui
    global currentFrameMillis
    global previousFrameMillis
    global sndSrv
    pygame.init()
    windowSize = windowWidth, windowHeight = 1280, 640
    surface = pygame.display.set_mode(windowSize, pygame.RESIZABLE)
    initUI()
    gui.setScreen(S_MAIN_MENU)
    sndSrv = SndSrv()
    doomMap = DoomMap(0, 0)
    doomMap.setSndSrv(sndSrv)
    renderer = DoomRenderer()
    renderer.setGUI(gui)
    renderer.setViewWidth(windowWidth)
    renderer.setViewHeight(windowHeight)
    physicsController = DoomPhysicsController()
    inputController = DoomInputController()
    inputController.setGUI(gui)
    mapLoader = DoomMapLoader()
    camera = DoomCamera()
    renderer.setMap(doomMap)
    renderer.setSurface(surface)
    renderer.setCamera(camera)
    player = DoomPlayer()
    camera.follow(player)
    player.setCamera(camera)
    gui.setPlayer(player)
    inputController.setPlayer(player)
    #startMap('testMap')
    camera.setCenter([windowWidth // 2, windowHeight // 2])
    player.setSndSrv(sndSrv)
    sndSrv.loadSound(W_BFG9000_SHOT, W_BFG9000_SHOT_PATH)
    sndSrv.loadSound(W_PISTOL_SHOT, W_PISTOL_SHOT_PATH)
    sndSrv.loadSound(W_SHOTGUN_SHOT, W_SHOTGUN_SHOT_PATH)
    sndSrv.loadSound(W_SUPERSHOTGUN_SHOT, W_SUPERSHOTGUN_SHOT_PATH)
    sndSrv.loadSound(W_ROCKET_LAUNCHER_SHOT, W_ROCKET_LAUNCHER_SHOT_PATH)
    sndSrv.loadSound(W_PLASMAGUN_SHOT, W_PLASMAGUN_SHOT_PATH)
    sndSrv.loadSound(P_PAIN, P_PAIN_PATH)
    sndSrv.loadSound(P_DEATH, P_DEATH_PATH)
    exiting = False
    showScreen(S_MAIN_MENU)
    clock = pygame.time.Clock()
    deltaTime = 0
    running = True
    currentFrameMillis = int(round(time() * 1000))
    previousFrameMillis = int(round(time() * 1000))

def showScreen(screen):
    global mainMenu
    global episodeChoice
    global difficultyChoice
    global exitChoice
    global win
    global lose
    global gui
    global gameUI
    global pauseScreen
    global sndSrv
    gui.setScreen(screen)
    if screen == S_MAIN_MENU:
        sndSrv.load_music('base\\a.ogg')
        sndSrv.start_music(0)
        player.initParameters()
        gui.setScreen(S_MAIN_MENU)
        gui.setNextScreen(None)
        gui.setElements(mainMenu)
    elif screen == S_EPISODE_CHOICE:
        gui.setElements(episodeChoice)
    elif screen == S_DIFFICULTY_CHOICE:
        gui.setElements(difficultyChoice)
    elif screen == S_EXIT:
        gui.setElements(exitChoice)
    elif screen == S_WIN:
        gui.setElements(win)
    elif screen == S_LOSE:
        gui.setElements(lose)
    elif screen == S_GAME:
        gui.setElements(gameUI)
    elif screen == S_PAUSED:
        gui.setElements(pauseScreen)


def initUI():
    global mainMenu
    global episodeChoice
    global difficultyChoice
    global exitChoice
    global win
    global lose
    global windowWidth, windowHeight
    global gui
    global gameUI
    global pauseScreen
    gui = GUI()
    mainMenu.append(ScreenChangeButton((windowWidth // 2 - 200, windowHeight // 2 - 100, 440, 100), 'NEW GAME', S_EPISODE_CHOICE, gui))
    mainMenu.append(ScreenChangeButton((windowWidth // 2 - 200, windowHeight // 2, 440, 100), 'LOAD GAME', S_LOAD_GAME, gui))
    mainMenu.append(ScreenChangeButton((windowWidth // 2 - 200, windowHeight // 2 + 100, 440, 100), 'EXIT', S_EXIT, gui))
    exitChoice.append(ExitButton((windowWidth // 2 - 100, windowHeight // 2 - 50, 200, 100), 'YES', gui))
    exitChoice.append(ScreenChangeButton((windowWidth // 2 + 100, windowHeight // 2 - 50, 200, 100), 'NO', S_MAIN_MENU, gui))
    episodeChoice.append(MapStartButton((windowWidth // 2 - 500, windowHeight // 2 - 50, 900, 100), 'KNEE-DEEP IN THE DEAD', S_GAME, gui, 'testMap'))
    gameUI.append(Label((230, windowHeight - 150, 0, 100), 'health', gui))
    gameUI.append(Label((825, windowHeight - 150, 0, 125), 'armor', gui))
    gameUI.append(Label((50, windowHeight - 150, 0, 100), 'ammo', gui))
    gameUI.append(Label((437, windowHeight - 152, 0, 60), '2', gui, text_color=(255, 255, 0)))
    gameUI.append(Label((487, windowHeight - 152, 0, 60), '3', gui, text_color=(255, 255, 0)))
    gameUI.append(Label((537, windowHeight - 152, 0, 60), '4', gui, text_color=(255, 255, 0)))
    gameUI.append(Label((437, windowHeight - 102, 0, 60), '5', gui, text_color=(255, 255, 0)))
    gameUI.append(Label((487, windowHeight - 102, 0, 60), '6', gui, text_color=(255, 255, 0)))
    gameUI.append(Label((537, windowHeight - 102, 0, 60), '7', gui, text_color=(255, 255, 0)))
    gameUI.append(Label((1100, windowHeight - 140, 0, 50), '0', gui, text_color=(255, 255, 0)))
    gameUI.append(Label((1100, windowHeight - 110, 0, 50), '0', gui, text_color=(255, 255, 0)))
    gameUI.append(Label((1100, windowHeight - 80, 0, 50), '0', gui, text_color=(255, 255, 0)))
    gameUI.append(Label((1100, windowHeight - 50, 0, 50), '0', gui, text_color=(255, 255, 0)))
    gameUI.append(Label((1200, windowHeight - 140, 0, 50), '0', gui, text_color=(255, 255, 0)))
    gameUI.append(Label((1200, windowHeight - 110, 0, 50), '0', gui, text_color=(255, 255, 0)))
    gameUI.append(Label((1200, windowHeight - 80, 0, 50), '0', gui, text_color=(255, 255, 0)))
    gameUI.append(Label((1200, windowHeight - 50, 0, 50), '0', gui, text_color=(255, 255, 0)))
    gameUI.append(Label((0, 0, 0, 50), '', gui, text_color=(255, 0, 0)))
    gameUI.append(Label((0, 50, 0, 50), '', gui, text_color=(255, 0, 0)))
    pauseScreen.append(PauseReturnButton((windowWidth // 2 - 200, windowHeight // 2 - 50, 400, 100), 'RETURN', S_GAME, gui))
    lose.append(Label((windowWidth // 2 - 200, windowHeight // 2 - 200, 0, 100), 'YOU\'VE LOST', gui, text_color=(255, 0, 0)))
    lose.append(ScreenChangeButton((windowWidth // 2 - 200, windowHeight // 2, 440, 100), 'MAIN MENU', S_MAIN_MENU, gui))
    win.append(
        Label((windowWidth // 2 - 200, windowHeight // 2 - 200, 0, 100), 'YOU\'VE WON', gui, text_color=(255, 0, 0)))
    win.append(
        ScreenChangeButton((windowWidth // 2 - 200, windowHeight // 2, 440, 100), 'MAIN MENU', S_MAIN_MENU, gui))


#def checkCollision(x, y):
#    global doomMap
#    return doomMap.getCollision(x, y)

def startMap( name ):
    global doomMap
    global renderer
    global physicsController
    global inputController
    global mapLoader
    global camera
    global player
    doomMap = DoomMap(0, 0)
    doomMap.loadMapData(mapLoader.loadMapFromFile('base\\' + name + '.dm'))
    things = mapLoader.loadThingsFromFile('base\\' + name + '.dt')
    doomMap.loadThingsData(things)
    tileImagePaths = mapLoader.loadTileImagePaths('base\\' + name + '.ip')
    doomMap.loadTileImages(tileImagePaths)
    thingsImagePaths = mapLoader.loadThingsImagePaths('base\\' + name + '.ti')
    doomMap.loadThingsImages(thingsImagePaths)
    doomMap.loadCollisionData(mapLoader.loadCollisionFromFile('base\\' + name + '.cd'))
    doomMap.loadMapSpecials(mapLoader.loadMapSpecials('base\\' + name + '.sd'))
    physicsController.setThings(things)
    renderer.setMap(doomMap)
    camera.follow(player)
    player.setCamera(camera)
    doomMap.addThing(player)
    print(name)
    for thing in things:
        thing.setDoomMap(doomMap)
        if type(thing) is Monster:
            thing.setPlayer(player)
        thing.updateImageParameters()


def doomMainLoop():
    global windowSize, windowWidth, windowHeight, surface
    global doomMap
    global renderer
    global clock, deltaTime
    global exiting, running
    global physicsController
    global inputController
    global camera
    global gui
    global currentFrameMillis
    global previousFrameMillis
    global sndSrv
    while not exiting:
        currentFrameMillis = int(round(time() * 1000))
        deltaTime = (currentFrameMillis - previousFrameMillis) * TIME_COEFFICIENT
        previousFrameMillis = currentFrameMillis
        surface.fill((0, 0, 0))
        camera.updateMovement()
        renderer.render()
        if running:
            physicsController.updateMovement(deltaTime)
            doomMap.processProjectiles(deltaTime)
        gameUI[0].setText(str(int(player.getHealth())) + '%')
        gameUI[1].setText(str(int(player.getArmor())) + '%')
        gameUI[2].setText(str(player.getCurrentAmmo()))
        if player.hasWeapon(W_PISTOL):
            gameUI[3].setText('2')
        else:
            gameUI[3].setText('')
        if player.hasWeapon(W_SHOTGUN) or player.hasWeapon(W_SUPERSHOTGUN):
            gameUI[4].setText('3')
        else:
            gameUI[4].setText('')
        if player.hasWeapon(W_CHAINGUN):
            gameUI[5].setText('4')
        else:
            gameUI[5].setText('')
        if player.hasWeapon(W_ROCKET_LAUNCHER):
            gameUI[6].setText('5')
        else:
            gameUI[6].setText('')
        if player.hasWeapon(W_PLASMAGUN):
            gameUI[7].setText('6')
        else:
            gameUI[7].setText('')
        if player.hasWeapon(W_BFG9000):
            gameUI[8].setText('7')
        else:
            gameUI[8].setText('')
        gameUI[9].setText(str(player.getAmmo(A_BULLETS)))
        gameUI[10].setText(str(player.getAmmo(A_SHELLS)))
        gameUI[11].setText(str(player.getAmmo(A_ROCKETS)))
        gameUI[12].setText(str(player.getAmmo(A_CELLS)))
        gameUI[13].setText(str(player.getMaxAmmo(A_BULLETS)))
        gameUI[14].setText(str(player.getMaxAmmo(A_SHELLS)))
        gameUI[15].setText(str(player.getMaxAmmo(A_ROCKETS)))
        gameUI[16].setText(str(player.getMaxAmmo(A_CELLS)))
        text = player.getTextToDisplay()
        if len(text) >= 2:
            gameUI[17].setText(text[-2][0])
            gameUI[18].setText(text[-1][0])
        elif len(text) == 1:
            gameUI[17].setText(text[-1][0])
            gameUI[18].setText('')
        else:
            gameUI[17].setText('')
            gameUI[18].setText('')
        pygame.display.flip()
        for event in pygame.event.get():
            exiting = inputController.processInput(event)
        if player.isMapFinished():
            player.setMapFinished(False)
            if doomMap.isEnding:
                running = False
                showScreen(S_WIN)
            else:
                startMap(player.getNextMap())
        if player.isDead():
            if gui.getScreen() == S_GAME:
                running = False
                showScreen(S_LOSE)
        elif player.getPaused():
            running = False
            showScreen(S_PAUSED)
        else:
            running = True
        if gui.getNextScreen() is not None:
            showScreen(gui.getNextScreen())
            gui.setScreen(gui.getNextScreen())
            gui.setNextScreen(None)
        if gui.getNextMap() is not None:
            startMap(gui.getNextMap())
            gui.setNextMap(None)
        if gui.getExiting():
            exiting = True
    sndSrv.onExit()


doomInit()
doomMainLoop()