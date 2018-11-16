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
 REFERENCE
 	sys.stdout: http://mynthon.net/howto/-/python/python%20-%20docs%20-%20sys.stdout.write%20-%20print%20without%20new%20lines.txt
 	reading and writing files: https://www.guru99.com/reading-and-writing-files-in-python.html
 	generate random string: https://pythontips.com/2013/07/28/generating-a-random-string/
 	lowercase characters: https://docs.python.org/2/library/string.html
"""

def fileWriteRandom(file_name) :
	rando_string = ''.join([random.choice(string.ascii_lowercase) for i in range (10)])
	rando_string += '\n'
	file_name.write(rando_string)
	sys.stdout.write(rando_string) 
	file_name.close()
	return

def numberOperations() :
	rando1 = random.randint(1,43)
	rando2 = random.randint(1,43)

	rando_sum = rando1+rando2

	print(rando1)
	print(rando2)
	print(rando_sum)
	return

def main():

	file1 = open("ABC.txt","w+")
	file2 = open("123.txt", "w+")
	file3 = open("doRayMe.txt", "w+")

	fileWriteRandom(file1)
	fileWriteRandom(file2)
	fileWriteRandom(file3)
	
	numberOperations()

if __name__ == "__main__":
	main()