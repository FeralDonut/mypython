#!/usr/bin/python
"""
 Reference
	https://www.guru99.com/reading-and-writing-files-in-python.html
"""

import random
import string
import sys


"""
 NAME
    fileWriteRandom
 SYNPOSIS
    Takes in the name of a file to be written to
 DESCRIPTION
    writes 10 random lowercase letters to a file passed in
    adds a new line to that string as the 11th character
    writes the line to standard out and closes the file
"""

def fileWriteRandom(file_name) :
	rando_string = ''.join([random.choice(string.ascii_lowercase) for i in range (10)])
	rando_string += '\n'
	file_name.write(rando_string)
	sys.stdout.write(rando_string) 
	file_name.close()
	return

def main():

	file1 = open("ABC.txt","w+")
	file2 = open("123.txt", "w+")
	file3 = open("doRayMe.txt", "w+")

	fileWriteRandom(file1)
	fileWriteRandom(file2)
	fileWriteRandom(file3)
		

if __name__ == "__main__":
	main()