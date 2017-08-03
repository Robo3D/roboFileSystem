import sys
import os

class AbstractFile(object):

    def __init__(self, directory, newname):
        self.directory = directory
        self.newname = newname
        self.fileArr = []
        with open(directory, 'r') as aFile:
            for line in aFile:
                self.fileArr.append(line)



    def editFile(self):
        print("hello")
        with open(self.directory, 'r+') as fileObj:
            text = fileObj.read()
