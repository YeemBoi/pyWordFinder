print("Please paste the file path of your dictionary file. This file contains a list of words.")
dictPath = input()

print("Please paste the file path of the pyWordFinder folder.")
path = input()
pyPath = path + "/wordFind.py"
execPath = path[0:path.rfind("/")] + "/wordFind.bat"
startPy = open(pyPath, "rt")
startText = startPy.read()
allText = 'dictionary = open("'+dictPath+'", "rt")\n' + startText

startPy = open(pyPath, "wt")
startPy.write(allText)
startPy.close()

exec = open(execPath, "wt")
exec.write("python3 " + pyPath)
exec.close()
print("Done! Your  program should be ready to use at", execPath)
