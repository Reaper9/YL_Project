class DoomClass:
    def __init__(self):
        self.parameters = None
        self.initParameters()

    def initParameters(self):
        self.parameters = {}

    def validateConstant(self, constantName):
        return False

    def setParameter(self, parameterName, newVal):
        if self.validateConstant(parameterName):
            if type(newVal) is bool:
                self.parameters[parameterName] = newVal
            else:
                pass

    def getParameter(self, parameterName):
        if self.validateConstant(parameterName):
            return self.parameters[parameterName]
