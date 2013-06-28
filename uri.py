import re
class Uri:
    def __init__(self):
        self.uri = ""
        self.length = len(self.uri)
    def __init__(self, uriStr):
        self.uri = uriStr
        self.length = len(self.uri)

    def show(self):
        print self.uri

    def addPath(self, pathStr):
        if self.uri[self.length - 1] == "/":
            if pathStr[0] == "/":
                self.uri += pathStr[1:]
            else:
                self.uri += pathStr
        else:
            if pathStr[0] == "/":
                self.uri += pathStr
            else:
                self.uri += "/" + pathStr
        self.length = len(self.uri)
        return self

    def addFile(self, filePathStr):
       return self.addPath(filePathStr)

if __name__ == "__main__":
    s1 = "http://saiwarang.com"
    u1 = Uri(s1)
    u1.show()
    a1 = "/resume.pdf"
    a2 = "posts"
    u1.addPath(a2).addFile(a1)
    u1.show()



