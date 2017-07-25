import subprocess
import sys
import os

class FileSystem(object):

    #The class only needs an appropriate .img file
    #to operate. It creates mount points based on the
    #file name of the .img file
    def __init__(self, image, piaddress, blobfile):
        #the directory address is reversed due to the .img file name
        #being at the end of it
        tempDirec = image[len(image)::-1]
        actualIMG = ""
        counter = len(image) - 1
        iterate = 0
        while(counter >= 0):
            if tempDirec[iterate] != "/":
                actualIMG = actualIMG + tempDirec[iterate]
                iterate += 1
                counter -= 1
            else:
                break
        actualIMG = actualIMG[len(actualIMG)::-1]
        self.image = actualIMG

        #self.valid can be thought of as a boolean variable,
        #where 1 is true and 0 is false. It is used to keep
        #track of the validity of the file in future operations.
        self.valid = 0
        self.rsync = piaddress
        self.blobfile = blobfile
        #if it is a valid file, print out the directory address
        #and set the calid bit to true
        if '.img' in self.image:
            print("Image file selected: " + self.image)
            self.valid = 1
        #else if it is not valid, do not continue any further operations
        else:
            print("Invalid image file selcted, aborting")
        #it then proceeds to create two seperate mount points
        #and even goes ahead and validates them through the mkdir command
        self.mountone = self.image + "1"
        self.mounttwo = self.image + "2"
        if self.valid == 1:
            print(" ")
            os.system('mkdir ' + self.mountone + ' ' + self.mounttwo)
        else:
            os.system('rm -rf ' + self.mountone)
            os.system('rm -rf ' + self.mounttwo)

    #bash command to mount the actual file in the form of a method
    def mountIMG(self):
        if self.valid == 1:
            print(" ")
            os.system('sudo mount -v -o offset=4194304 -t vfat '+ self.image + ' ' + self.mountone)

            print(" ")
            print(self.image + " is mounted at: ")
            os.system('pwd')
            print(" ")

    #bash command to unmount the file in the form of a method
    def unmountIMG(self):
        if self.valid == 1:
            os.system('sudo umount ' + self.mountone)
            print(self.image + " is no longer mounted")
            
    #bash sequence to mount, rsync, and unmount the selected image
    def rsync(self):
        if self.valid == 1:
            print(" ")
            self.mountIMG()
            if self.blobfile != "":
                os.system('rsync --progress -av --exclude-from=' + self.blobfile + ' --rsh="ssh" ' + self.rsync + ' ' + self.mountone)
            else:
                os.system('rsync --progress -av --rsh="ssh" ' + self.rsync + ' ' + self.mountone)
        
    
#where the program actually runs
if __name__=='__main__':
    print(" ")
    print("------------------------------")
    print("------roboGenesis v1.0--------")
    print("------------------------------")
    print(" ")
    imageFile = sys.argv[1]
    piAddress = sys.argv[2]
    blob = sys.argv[3]
    fs = FileSystem(imageFile, piAddress, blob)
    fs.mountIMG()
    fs.unmountIMG()
