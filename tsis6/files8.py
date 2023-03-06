import os


class FileManager:
    def __init__(self, fname):
        self.fname = fname


    def checkFile(self):
        if os.path.exists("{file_name}.txt".format(file_name=self.fname)):
            return True
        else:
            return False


    def removeFile(self):
        if self.checkFile():
            os.remove("{file_name}.txt".format(file_name=self.fname))
        else:
            print("The file does not exist")

manager = FileManager("A")
manager.removeFile()
