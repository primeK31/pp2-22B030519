import os


def checkFile(fname):
    if os.path.exists("{file_name}.txt".format(file_name=fname)):
        return True
    else:
        return False

def createFile(fname):
    if checkFile(fname):
        print("File is already exist")
    else:
        print('*******************')
        f = open("{file_name}.txt".format(file_name=fname), "x")
        print('*******************')

def readFile(fname):
    if checkFile(fname):
        print('*******************')
        f = open("{file_name}.txt".format(file_name=fname), "r")
        print(f.read())
        f.close()
        print('*******************')
    else:
        print("This file doesn't exist")

def appendFile(fname):
    if checkFile(fname):
        print('*******************')
        f = open("{file_name}.txt".format(file_name=fname), "r")
        l = list()
        for i in f:
            l.append(i)
        while True:
            line = input()
            if line:
                l.append(line)
            else:
                break
        f.close()
        f = open("{file_name}.txt".format(file_name=fname), "w")
        text = '\n'.join(l)
        f.write(text)
        f.close()
        print('*******************')
    else:
        print("This file doesn't exist")

def overwriteFile(fname):
    if checkFile(fname):
        print('*******************')
        f = open("{file_name}.txt".format(file_name=fname), "w")
        contents = list()
        while True:
            line = input()
            if line:
                contents.append(line)
            else:
                break
        text = '\n'.join(contents)
        f.write(text)
        f.close()
        print('*******************')
    else:
        print("This file doesn't exist")

def removeFile(fname):
    if checkFile(fname):
        os.remove("{file_name}.txt".format(file_name=fname))
    else:
        print("The file does not exist")


print('Welcome to my blog!\nWhat do you want to do with files/the file?')

while True:
    option = int(input('Options(type a number):\n1-Create a new file\n2-Read existing file\n3-Update some information in a file\n4-Overwrite all content in a file\n5-Remove existing file\nWrite a number(1-5): '))
    if option == 0:
        break
    file_name = input('Please enter a file name (no extension, .txt will be added automatically):').strip()
    if option == 1:
        createFile(file_name)
    elif option == 2:
        readFile(file_name)
    elif option == 3:
        appendFile(file_name)
    elif option == 4:
        overwriteFile(file_name)
    elif option == 5:
        removeFile(file_name)
    else:
        break
else:
    print('Something went wrong!')
