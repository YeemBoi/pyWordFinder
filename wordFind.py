dupeDict = dict()
guesses = []
words = []
baseStr = ""

print('What mode would you like? Send:\n"0" for normal mode\n"1" for cutting mode\n"2" for swapping mode')
mode = int(input())


def getAnswer(message = "Would you like the output to be sorted by length?"):
	print(message)
	userAnswer = input().lower()
	if "y" in userAnswer: return True
	elif "n" in userAnswer: return False
	else: return getAnswer("Sorry, I don't understand. Try rephrasing your answer.")


def checkStr (inputStr):
	usedLetters = ""
	for char in inputStr:
		if char in baseStr and usedLetters.count(char) < dupeDict[char]:
			usedLetters += (char)
		else: return False
	return True


def checkArr ():
	for line in dictionary:
		if line[0] in baseStr:
			for word in guesses:
				if word == line:
					words.append(word[0:len(word)-1])
					guesses.remove(word)


def showWord(foundWord):
	print(foundWord[0] + foundword[1:len(foundword)].lower())

def orderedPrint ():
	for requestLength in range(baseLength-1, 1, -1):
		print()
		print(requestLength, "letter words:")
		for word in words:
			if len(word) == requestLength:
				showWord(word)


def showResults ():
	lengthSort = getAnswer()
	
	print("\n")
	
	if lengthSort == False:
		for word in words: showWord(word)
	else: orderedPrint()



if mode == 1:
	print("Enter your word!")
	baseStr = input().upper()
	baseLength = len(baseStr)
	for startCut in range(baseLength):
		for endCut in range(startCut +1, baseLength +1):
			guesses.append(baseStr[startCut:endCut] + "\n")
	
	checkArr()
	showResults()
	
elif mode == 2: print("Feature not finished yet. Sorry!")"""
	print("Enter your word!")
	baseStr = input().upper()
	usedWords = [baseStr]
	loopedWords = []
	tracker = 0
	tracker += check(baseStr)
	letterLength = len(baseStr)
	combinations = factorialize(baseStr)

	for i in range(combinations):
		if i < len(usedWords):
			currentStr = usedWords[i]
			if not (currentStr in loopedWords):
				loopedWords.add(currentStr)
				for iA in range(letterLength-1):
					for iB in range(iA + 1, letterLength):
						swapoutput = ""
						iE = 0
						for outConnect in currentStr:
							if iE == iB:
								swapOutput += currentStr[iA]
							elif iE == iA:
								swapOutput += currentStr[iB]
							else:
								swapOutput += outConnect
							iE += 1
						tracker += check(swapOutput)
		if tracker >= combinations: break"""

else:
	print("Please enter your letters. No spaces.")
	baseStr = input().upper() + "\n"

	baseLength = len(baseStr)

	for letter in baseStr:
		dupeDict[letter] = baseStr.count(letter)
		
	for line in dictionary:
		lineLength = len(line)
		if lineLength <= baseLength:
			if checkStr(line) == True: words.append(line[0:lineLength-1])
	
	showResults()

#if (getAnswer("\n\nExit?")) == True: print("yeet") #sys.exit()
