from doomClass import DoomClass
from pygame import mixer

class SndSrv(DoomClass):

    def __init__(self):
        mixer.pre_init()
        mixer.init()
        self.sounds = {}

    def pauseSounds(self):
        mixer.pause()

    def resumeSounds(self):
        mixer.unpause()

    def onExit(self):
        mixer.quit()

    def loadSound(self, name, path):
        if not name in self.sounds:
            self.sounds[name] = mixer.Sound(path)

    def startSound(self, name):
        self.sounds[name].play()

    def stopSound(self, name):
        self.sounds[name].stop()

    def load_music(self, path):
        mixer.music.load(path)

    def start_music(self, loops):
        mixer.music.play(loops)

    def stop_music(self):
        mixer.music.stop()

    def pause_music(self):
        mixer.music.pause()