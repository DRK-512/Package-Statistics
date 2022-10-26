#!/usr/bin/python3
import sys # For the input param 
import wget # For wget command on URL
import pathlib # checking if file exists
import gzip # extract .gz file
import shutil # open the content of .gz file

############################################################################
# 						    Helper Functions                               #
############################################################################

# this will check the architecture inputted, if it is not valid, the code ends
def checkArch(input):
	if not ((input=="amd64") or (input=="arm64") or (input=="armel") or (input=="armhf") or
	(input=="i386") or (input=="mips64el") or (input=="mipsel") or (input=="ppc64el") or
	(input=="s390x")):
		print(input+" is not a valid architecture, please input a valid one")
		print("Here is a list of valid architectures for this script: ")
		print("amd64\narm64\narmel\narmhf\ni386\nmips64el\nmipsel\nppc64el\ns390x")
		quit()

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
	
# first we check if we input a valid architecture
checkArch(arch)
#print("ARCH VALID")

# Now we will fetch the contents file, but first we check if it's already fetched
file = pathlib.Path('./Contents-'+arch+'.gz')
if not file.exists ():
	print("Now pulling Contents-"+arch+".gz")
	url = 'http://ftp.uk.debian.org/debian/dists/stable/main/Contents-'+arch+'.gz'
	wget.download(url)
	
# Now we extract the package, but first check if it exists
file = pathlib.Path('./Contents-'+arch)
if not file.exists ():
	print("Now extracting Contents-"+arch+" ...")
	with gzip.open('./Contents-'+arch+'.gz', 'rb') as f_in:
		with open('Contents-'+arch, 'wb') as f_out:
		    shutil.copyfileobj(f_in, f_out)



