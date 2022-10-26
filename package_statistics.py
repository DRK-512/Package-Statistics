#!/usr/bin/python3
import sys 		# For the input param 
import wget 	# For wget command on URL
import pathlib 	# checking if file exists
import gzip 	# extract .gz file
import shutil 	# open the content of .gz file

############################################################################
# 						    Helper Functions                               #
############################################################################

# this will check the user's input architecture, and see if it is not valid
def checkArch(input):
	if not ((input=="amd64") or (input=="arm64") or (input=="armel") or (input=="armhf") or
	(input=="i386") or (input=="mips64el") or (input=="mipsel") or (input=="ppc64el") or
	(input=="s390x")):
		# If architecture is not valid, we end the script
		print(input+" is not a valid architecture, please input a valid one")
		print("Here is a list of valid architectures for this script: ")
		print("amd64\narm64\narmel\narmhf\ni386\nmips64el\nmipsel\nppc64el\ns390x")
		quit()

# Used to fetch the .gz file 
def fetcher(input):
	file = pathlib.Path('./Contents-'+input+'.gz')
	# first check if it exists, if it does, then we skip this
	if not file.exists ():
		print("Now pulling Contents-"+input+".gz")
		url = 'http://ftp.uk.debian.org/debian/dists/stable/main/Contents-'+input+'.gz'
		wget.download(url)

# Used to extract the .gz file
def extractor(input): 
	# first check if it exists, if it does, then we skip this
	file = pathlib.Path('./Contents-'+input)
	if not file.exists ():
		print("\nNow extracting Contents-"+input+" ...")
		with gzip.open('./Contents-'+input+'.gz', 'rb') as f_in:
			with open('Contents-'+input, 'wb') as f_out:
				shutil.copyfileobj(f_in, f_out)	
				
############################################################################
# 							  Main Function                                #
############################################################################

arch=""
try: 
	arch = sys.argv[1] # I only care about the first input
except:
	# If the user did not input something, they will know  
	print("Please enter an archtecture whilst running the program")
	print("EXAMPLE RUN: $ ./package_statistics.py <architecture name> ")
	quit()
	
# first we check if a valid architecture was given
checkArch(arch)

# Now we will fetch the Contents-arch
fetcher(arch)
	
# Now we extract the package, but first check if it exists
extractor(arch)




