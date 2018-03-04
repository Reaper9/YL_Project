import pygame


class Label:
    def __init__(self, rect, text, gui, text_color = pygame.Color("red"), background_color = (141, 141, 141, 0) ):
        self.rect = pygame.Rect(rect)
        self.text = text
        if background_color == -1:
            self.bgcolor = ( 0, 0, 0, 0 )
        else:
            self.bgcolor = background_color
        self.font_color = text_color
        self.font = pygame.font.Font(None, self.rect.height - 4)
        self.rendered_text = None
        self.rendered_rect = None
        self.gui = gui


    def render(self, surface):
        surface.fill(self.bgcolor, self.rect)
        self.rendered_text = self.font.render(self.text, False, self.font_color)
        self.rendered_rect = self.rendered_text.get_rect(x=self.rect.x + 2, centery=self.rect.centery)
        surface.blit(self.rendered_text, self.rendered_rect)

    def setText(self, text):
        self.text = text


class GUI:
    def __init__(self):
        self.elements = []
        self.nextScreen = None
        self.screen = None
        self.nextMap = None
        self.exiting = False
        self.player = None

    def add_element(self, element):
        self.elements.append(element)

    def render(self, surface):
        for element in self.elements:
            render = getattr(element, "render", None)
            if callable(render):
                element.render(surface)

    def update(self):
        for element in self.elements:
            update = getattr(element, "update", None)
            if callable(update):
                element.update()
            onButtonPressed = getattr( element, 'onButtonPressed', None )
            if callable( onButtonPressed ) and element.pressed:
                element.onButtonPressed()

    def get_event(self, event):
        result = False
        for element in self.elements:
            get_event = getattr(element, "get_event", None)
            if callable(get_event):
                result = element.get_event(event)
        return result

    def setNextScreen(self, screen):
        self.nextScreen = screen

    def getNextScreen(self):
        return self.nextScreen

    def setElements(self, elements):
        self.elements = elements

    def getScreen(self):
        return self.screen

    def setScreen(self, screen):
        self.screen = screen

    def setNextMap(self, nextMap):
        self.nextMap = nextMap

    def getNextMap(self):
        return self.nextMap

    def setExiting(self, exiting):
        self.exiting = exiting

    def getExiting(self):
        return self.exiting

    def setPlayer(self, player):
        self.player = player

    def getPlayer(self):
        return self.player


class Button(Label):
    def __init__(self, rect, text, gui):
        super().__init__(rect, text, gui)
        self.bgcolor = pygame.Color("blue")
        self.pressed = False
        self.processText()

    def render(self, surface):
        surface.fill(self.bgcolor, self.rect)
        self.rendered_text = self.font.render(self.text, 1, self.font_color)
        if not self.pressed:
            color1 = pygame.Color("white")
            color2 = pygame.Color("black")
            self.rendered_rect = self.rendered_text.get_rect(x=self.rect.x + 5, centery=self.rect.centery)
        else:
            color1 = pygame.Color("black")
            color2 = pygame.Color("white")
            self.rendered_rect = self.rendered_text.get_rect(x=self.rect.x + 7, centery=self.rect.centery + 2)

        pygame.draw.rect(surface, color1, self.rect, 2)
        pygame.draw.line(surface, color2, (self.rect.right - 1, self.rect.top), (self.rect.right - 1, self.rect.bottom), 2)
        pygame.draw.line(surface, color2, (self.rect.left, self.rect.bottom - 1),
                         (self.rect.right, self.rect.bottom - 1), 2)
        surface.blit(self.rendered_text, self.rendered_rect)

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.pressed = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.pressed = False
        return True

    def processText(self):
        textWidth, textHeight = self.font.size( self.text )
        if textWidth >= self.rect.width:
            self.text += '...'
        while textWidth >= self.rect.width:
            self.text = self.text[: -4] + self.text[-3 : len( self.text )]
            textWidth, textHeight = self.font.size(self.text)

    def process(self):
        pass


class ScreenChangeButton(Button):

    def __init__(self, rect, text, screen, gui):
        super(ScreenChangeButton, self).__init__(rect, text, gui)
        self.screen = screen

    def render(self, surface):
        surface.fill(self.bgcolor, self.rect)
        self.rendered_text = self.font.render(self.text, 1, self.font_color)
        if not self.pressed:
            color1 = pygame.Color("white")
            color2 = pygame.Color("black")
            self.rendered_rect = self.rendered_text.get_rect(x=self.rect.x + 5, centery=self.rect.centery)
        pygame.draw.rect(surface, color1, self.rect, 2)
        pygame.draw.line(surface, color2, (self.rect.right - 1, self.rect.top), (self.rect.right - 1, self.rect.bottom),
                         2)
        pygame.draw.line(surface, color2, (self.rect.left, self.rect.bottom - 1),
                         (self.rect.right, self.rect.bottom - 1), 2)
        surface.blit(self.rendered_text, self.rendered_rect)

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.rect.collidepoint(event.pos):
            self.gui.setNextScreen(self.screen)
            return True
        return False

class MapStartButton(ScreenChangeButton):

    def __init__(self, rect, text, screen, gui, startingMap):
        super(MapStartButton, self).__init__(rect, text, screen, gui)
        self.startingMap = startingMap

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.rect.collidepoint(event.pos):
            self.gui.setNextScreen(self.screen)
            self.gui.setNextMap(self.startingMap)
            return True
        return False

class ExitButton(Button):

    def __init__(self, rect, text, gui):
        super(ExitButton, self).__init__(rect, text, gui)

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.rect.collidepoint(event.pos):
            self.gui.setExiting(True)
            return True
        return False

class PauseReturnButton(ScreenChangeButton):

    #def __init__(self, rect, text, screen, gui):
    #    super(PauseReturnButton, self).__init__(rect, text, screen, gui)

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.rect.collidepoint(event.pos):
            self.gui.setNextScreen(self.screen)
            self.gui.getPlayer().setPaused(False)
            return True
        return False