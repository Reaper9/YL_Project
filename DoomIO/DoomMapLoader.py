from pydoc import locate
from DoomMap.MapSpecial import *
from doomUtils import get_class


class DoomMapLoader:

    def __init__(self):
        self.readingThingData = False
        pass

    def loadMapFromFile(self, mapPath):
        mapData = []
        with open(mapPath) as mapInput:
            mapName = mapInput.readline().rstrip('\n')
            mapWidth, mapHeight = mapInput.readline().rstrip('\n').split(' ')
            mapWidth, mapHeight = int(mapWidth), int(mapHeight)
            startX, startY = mapInput.readline().rstrip('\n').split(' ')
            startX, startY = int(startX), int(startY)
            mapMusic = mapInput.readline().rstrip('\n')
            isEndMap = mapInput.readline().rstrip('\n')
            line = ''
            for row in range(mapHeight):
                line = mapInput.readline().rstrip('\n').split(' ')
                mapData.append(list(map(int, line)))
        return [mapName, mapWidth, mapHeight, startX, startY, mapMusic, isEndMap, mapData]

    def loadCollisionFromFile(self, mapPath):
        mapData = []
        with open(mapPath) as mapInput:
            mapWidth, mapHeight = mapInput.readline().rstrip('\n').split(' ')
            mapWidth, mapHeight = int(mapWidth), int(mapHeight)
            line = ''
            for row in range(mapHeight):
                line = mapInput.readline().rstrip('\n').split(' ')
                mapData.append(list(map(int, line)))
        return [mapWidth, mapHeight, mapData]

    def loadThingsFromFile(self, thingsPath):
        thingsData = []
        with open(thingsPath) as thingsInput:
            line = thingsInput.readline().rstrip('\n')
            thing = None
            while line != '':
                if line.startswith('#') or line.startswith('//'):
                    pass
                elif line.startswith('THING'):
                    thing = get_class(line.split(' ')[1])()
                elif line.startswith('END_THING'):
                    thingsData.append(thing)
                elif line.startswith('set '):
                    line = line.split(' ', maxsplit=3)
                    setattr(thing, line[1], locate(line[2])(line[3]))
                elif line.startswith('call '):
                    line = line.split(' ')
                    getattr(thing, line[1])()
                elif line.startswith('func '):
                    line = line.split(' ', maxsplit=3)
                    getattr(thing, line[1])(locate(line[2])(line[3]))
                line = thingsInput.readline().rstrip('\n')
        return thingsData

    def loadTileImagePaths(self, path):
        paths = []
        with open(path) as inp:
            for i in range(int(inp.readline().rstrip('\n'))):
                paths.append(inp.readline().rstrip('\n'))
        return paths

    def loadThingsImagePaths(self, path):
        paths = {}
        with open(path) as inp:
            line = ''
            for i in range(int(inp.readline().rstrip('\n'))):
                line = inp.readline().rstrip('\n').split(' ')
                paths[line[0]] = line[1]
        return paths

    def loadMapSpecials(self, mapPath):
        specialsData = {}
        with open(mapPath) as specialsInput:
            line = specialsInput.readline().rstrip('\n')
            while line != '':
                if line.startswith('#') or line.startswith('//'):
                    pass
                else:
                    specialType, x, y = line.split(' ')
                    x, y = int(x), int(y)
                    if specialType == 'SECRET':
                        if (x, y) in specialsData:
                            specialsData[(x, y)].append(SecretSpecial())
                        else:
                            specialsData[(x, y)] = [SecretSpecial()]
                        line = specialsInput.readline().rstrip('\n')
                        specialsData[(x, y)][-1].setID(int(line))
                    elif specialType == 'TELEPORT':
                        if (x, y) in specialsData:
                            specialsData[(x, y)].append(TeleportSpecial())
                        else:
                            specialsData[(x, y)] = [TeleportSpecial()]
                        line = specialsInput.readline().rstrip('\n').split(' ')
                        specialsData[(x, y)][-1].setDestination(int(line[0]), int(line[1]))
                    elif specialType == 'DAMAGING_FLOOR':
                        if (x, y) in specialsData:
                            specialsData[(x, y)].append(DamagingFloorSpecial())
                        else:
                            specialsData[(x, y)] = [DamagingFloorSpecial()]
                        line = specialsInput.readline().rstrip('\n')
                        specialsData[(x, y)][-1].setDamage(float(line))
                    elif specialType == 'EXIT_TILE':
                        if (x, y) in specialsData:
                            specialsData[(x, y)].append(ExitTile())
                        else:
                            specialsData[(x, y)] = [ExitTile()]
                        line = specialsInput.readline().rstrip('\n')
                        specialsData[(x, y)][-1].setDestinationMap(line)
                    elif specialType == 'EXIT_SWITCH':
                        if (x, y) in specialsData:
                            specialsData[(x, y)].append(ExitSwitch())
                        else:
                            specialsData[(x, y)] = [ExitSwitch()]
                        line = specialsInput.readline().rstrip('\n')
                        specialsData[(x, y)][-1].setDestinationMap(line)
                line = specialsInput.readline().rstrip('\n')
        return specialsData
