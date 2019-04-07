import os
os.chdir(os.path.dirname(__file__))
path = os.getcwd()

pyPath = path+"/wordFind.py"
execPath = path[0:path.rfind("/")]+"/wordFind.bat"
execBat = open(execPath, "wt")
execBat.write("python3 " + pyPath)
execBat.close()

startPy = open(path+"/src", "rt")
startText = startPy.read()
mainPy = open(pyPath, "wt")

print("Please paste the file path of your dictionary file. This file contains a list of words.")
dictPath = input()

allText = 'dictionary = open("' +dictPath+ '", "rt")\n' + startText
mainPy.write(allText)
mainPy.close()
print("Done! Your  program should be ready to use at", execPath)
