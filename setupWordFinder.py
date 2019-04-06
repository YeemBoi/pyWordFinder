print("Please paste the file path of your dictionary file. This file contains a list of words.")
dictPath = input()

print("Please paste the file path of the pyWordFinder folder.")
pyPath = input()
startPy = open(pyPath, "rt")
startText = startPy.read()
allText = 'dictionary = open("'+dictPath+'", "rt")\n' + startText

startPy = open(pyPath, "wt")
startPy.write(allText)
startPy.close()

execPath = pyPath[0:pyPath.rfind("/")] + "/wordFind.bat"
exec = open(execPath, "wt")
exec.write("python3 " + pyPath + "/wordFind.py")
exec.close()
print("Done! Your  program should be ready to use at", execPath)
