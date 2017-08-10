import sys
import os

# a simple class that represents an abstraction of
# certain files in order to make processing more efficient

# the class requires a directory to the specific file and
# a new name for the changed file

class AbstractFile(object):

    def __init__(self, directory, newname):
        self.directory = directory
        self.newname = newname
        self.fileArr = []
        with open(directory, 'r') as aFile:
            for line in aFile:
                self.fileArr.append(line)

# this function has the primary purpose of opening
# the file given in the DIRECTORY input and renaming it
# based on the whatever was given for NEWNAME

    def editFile(self):

        text = ''

        with open(self.directory, 'r+') as fileObj:
            text = fileObj.read()

        if "/hosts" in self.directory:
            oldname = self.fileArr[1][10:]
            text = re.sub(oldname, self.newname,fileObj)

        elif "/hostname" in self.directory:
            oldname = self.fileArr[0]
            text = re.sub(oldname, self.newname,fileObj)
            
         
        elif "/netconnectd.yaml" in self.directory:
            oldname = self.fileArr[4][8:]
            text = re.sub(oldname, self.newname,fileObj)
            oldname = self.fileArr[5][7:]
            text = re.sub(oldname, self.newname,fileObj)

        fileObj.seek(0)
        fileObj.write(text)
        fileObj.truncate()
