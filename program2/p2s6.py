#!/usr/bin/env python

def main():
	
	nDegF = raw_input("Please enter a temperture in Fahrenheit:")
	
	print "%0.1f Degrees Fahrenheit" % nDegF
	
	nDegC = ( nDegF - 32) * 5 / 9
	
	print "%0.1f Degrees Centigrade" % nDegC
	
if __name__ == "__main__":
	main()
