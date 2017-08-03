import sys
import os
import FileSystem
import AbstractFile


if __name__=='__main__':

    img = sys.argv[1]

    fs = FileSystem.FileSystem(img,'pi','')
    fs.mountIMG()

    #f = AbstractFile.AbstractFile('/etc/hosts', 'brandon')
    #oldname = f.fileArr[1][10:]
    #print(oldname)
