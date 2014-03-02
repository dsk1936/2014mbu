#!/usr/bin/env python3

import sys

def ftoc(sDegreeF):
	#...convert text entry to number value that can be used in equations
	nDegreeF = int(sDegreeF)

	#...convert temperature from F to Celsius
	nDegreeC = (nDegreeF - 32) * 5 / 9 
	
	return nDegreeC
	
def printTemp(nDegreeC):
	
	print ("Temperature in degrees C is:", nDegreeC)

def printMessage(nDegreeC, nDegreeF):
	if nDegreeC < 0:
		print ("Pack long underwear!")
	
	#...check for it being a hot day...
	if nDegreeF > 100:
		print ("Remember to hydrate!")

def askLoop():
	#...initialize looping variable, assume 'yes' as the first answer
	continueYN = "y"
	
	while continueYN == "y":
		#...get temperature input from the user
		sDegreeF = input("Enter next temperature in degrees Farenheight (F):")
		
		nDegreeC = ftoc(sDegreeF)
		
		printTemp(nDegreeC)
		
		printMessage(nDegreeC, int(sDegreeF))
		
		continueYN = input("Input another?")

def singleRun(sDegreeF):
	
	nDegreeC = ftoc(sDegreeF)
	 
	printTemp(nDegreeC)
	printMessage(nDegreeC,int(sDegreeF))
	
if __name__ == "__main__":
	if len(sys.argv) == 2:
		singleRun(sys.argv[1])
	else:
		askLoop()
	
#exit the program
