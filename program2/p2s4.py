#!/usr/bin/env python

def main():
	
	nDegF = 50
	
	print "%d Degrees Fahrenheit".format(nDegF)
	
	nDegC = ( nDegF - 32) * 5 / 9
	
	print "%d Degrees Centigrade" % nDegC
	
if __name__ == "__main__":
	main()
