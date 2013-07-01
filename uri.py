import re

class __uri__:
    def __init__(self):
        self.uri = ""
        self.length = 0

    def __init__(self, uri):
        self.uri = uri
        self.length = len(uri)

    def show(self):
        print self.uri



def create(uri):
    return __uri__(uri)


def addPath(uri,  pathStr):
    if uri[len(uri) - 1] == "/":
        if pathStr[0] == "/":
            uri += pathStr[1:]
        else:
            uri += pathStr
    else:
        if pathStr[0] == "/":
            uri += pathStr
        else:
            uri += "/" + pathStr
    return uri

def addFile(uri, filePathStr):
    return addPath(uri, filePathStr)


if __name__ == "__main__":
    s1 = "http://saiwarang.com"
    a1 = "/resume.pdf"
    a2 = "posts"
    print addPath(s1, a2)
    u1 = create(s1)
    u1.show()


