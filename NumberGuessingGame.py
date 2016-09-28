"""
Author: Sandeep Das
This program asks the user to guess a random number between 1 and 100
"""
import random
import os.path
import json
from sys import argv

def main():
	print "Hello There! Welcome!"
	playerName = str (raw_input("Please enter your user id: "))
	print "How are you doing %s?" %playerName

	checkUser(playerName) # chk if the user already exists?

def checkUser(playerName):
	if not checkIfFileExist():
		print "Looks like this is your first attempt %s. Let's begin" %playerName
		game(playerName)
	else:
		playerScore = readFile(playerName) # Check if the Paleyer already exists in the file, check for key as playerName
		print "Welcome back %s. Looks like your last score was %d. Let's play again. " %(playerName, max(playerScore))
		game(playerName)

		
def readFile(playerName):
	with open ('Score.txt') as fileOpen:
		playerDict = json.load(fileOpen)
		if playerDict.get(playerName):
			playerScore = playerDict.get(playerName)
			return (playerScore)
		else:
			playerScore = []
			return (playerScore) # here i am


def game(playerName):
	print "Guess a number between 1 and 100!"
	randomNumber = random.randint(1, 100)
	found = False
	attemptCounter = 0
	while not found:
			userGuess = input("Your Guess: ")
			if userGuess == randomNumber:
				print "That's the number!"
				found = True
			elif userGuess < randomNumber:
				print "Thats's not it. Try biggger.."
				attemptCounter += 1
			else:
				print "Thats's not it. Try smaller!" 
				attemptCounter += 1
	
	print "Congratulations, you found it in %s attempts."%str(attemptCounter+1)

	if not checkIfFileExist():
		playerScore = []
		playerScore.append(int(attemptCounter+1))
		writeScore(playerName, playerScore)
	else:
		playerScore =readFile(playerName)
		playerScore.append(int(attemptCounter+1))
	
		writeScore(playerName, playerScore)

	print "Have a goood day!"

def checkIfFileExist():
	if not os.path.isfile('Score.txt') or os.stat('Score.txt').st_size == 0:
		filePresent = False
	else:
		filePresent = True
	return (filePresent)

def writeScore(playerName, playerScore):
	if not checkIfFileExist():
		playerDict = {}
		playerDict[playerName] = playerScore

		with open ('Score.txt', 'w') as fileOpen:
			json.dump(playerDict, fileOpen)
			print "New Player %s data saved." %playerName
	else:
		with open ('Score.txt') as fileOpen:
			playerDict = json.load(fileOpen)
			playerDict[playerName] = playerScore
			with open ('Score.txt', 'w') as fileOpen:
				json.dump(playerDict, fileOpen)
			print "Player %s data saved." %playerName


if __name__ == "__main__":
	main()
