from Program import Program


class Apps(object):
    """docstring fo Apps."""

    def __init__(self, apps=[]):
        self.apps = apps

    @classmethod
    def fromTextFile(self, path):
        with open(path, 'r') as f:
            appString = f.read()
            appString = appString.split(',')
            appString = [x for x in appString if x.strip()]
            appList = [Program(x) for x in appString]
            return self(apps=appList)

    def getApps(self):
        return self.apps

    def addApp(self, path):
        p = Program(path)
        self.apps.append(p)

    def clearApps(self):
        self.apps = []

    def toString(self):
        string = ''
        for app in self.apps:
            if app != self.apps[-1]:
                string = string+app.getPath()+','
            else:
                string = string + app.getPath()
        return string

    def toTextFile(self):
        with open('save.txt', 'w') as f:
            text = self.toString()
            f.write(text)
