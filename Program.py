import subprocess


class Program(object):
    """docstring for ."""

    def __init__(self, path):
        self.path = path

    def openApp(self):
        self.process = subprocess.Popen(self.path)
        return self.process

    def getPath(self):
        return self.path

    def closeApp(self):
        self.process.terminate()
