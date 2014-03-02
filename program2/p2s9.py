#!/usr/bin/env python

def main():
	
	cont = "y" # init cont to start loop
	
	while cont.lower() != 'n':
		
		nDegF = float(raw_input("Please enter a temperture in Fahrenheit:"))
		
		print "%0.1f Degrees Fahrenheit" % nDegF
		
		nDegC = ( nDegF - 32) * 5 / 9
		
		print "%0.1f Degrees Centigrade" % nDegC
		
		if nDegC < 0:
			print "Bring a jacket. Brrrr!"
		elif nDegF > 100:
			print "Drink plenty of water. It's gonna be a hot one."
		else:
			print "Something in between..."
		
		cont = raw_input("Convert another temperature? [y/n]:")
		
if __name__ == "__main__":
	main()
