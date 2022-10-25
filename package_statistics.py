#!/usr/bin/python3
import sys # This is for the input param 



# This is my version of a switch case in python
def switchCase(input):
	if((input=="amd64") or (input=="arm64") or (input=="armel") or (input=="armhf") or
	(input=="i386") or (input=="mips64el") or (input=="mipsel") or (input=="ppc64el") or
	(input=="s390x")):
		print("VALID HEHE")
	else: 
		print(input+" is not a valid architecture, please input a valid one")
		print("Here is a list of valid architectures for this script: ")
		print("amd64\narm64\narmel\narmhf\ni386\nmips64el\nmipsel\nppc64el\ns390x")
		quit()

# This is my main function
arch=""
try: 
	arch = sys.argv[1] # I only care about the first input
except:
	# If the user did not input something, they will know  
	print("Please enter an archtecture whilst running the program")
	print("EXAMPLE RUN: $ ./package_statistics.py <architecture name> ")
	quit()
	
# This will use a switch case to check the architecture is valid
switchCase(arch)
print("ARCH VALID")
