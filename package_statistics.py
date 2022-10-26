#!/usr/bin/python3
import sys      # For the input param 
import wget     # For wget command on URL
import pathlib  # checking if file exists
import gzip     # extract .gz file
import shutil   # open the content of .gz file
import csv      # reading contents file

############################################################################
#                           Helper Functions                               #
############################################################################

# This will check the user's input architecture, and see if it is not valid
def checkArch(input):
	if not ((input=="amd64") or (input=="arm64") or (input=="armel") or (input=="armhf") or
	(input=="i386") or (input=="mips64el") or (input=="mipsel") or (input=="ppc64el") or
	(input=="s390x") or (input=="all")):
		# if architecture is not valid, end the script
		print(input+" is not a valid architecture, please input a valid one")
		print("Here is a list of valid architectures for this script: ")
		print("all\namd64\narm64\narmel\narmhf\ni386\nmips64el\nmipsel\nppc64el\ns390x")
		quit()

# Used to fetch the .gz file 
def fetcher(input):
	file = pathlib.Path('./Contents-'+input+'.gz')
	# first check if it exists, if it does, then we skip this
	if not file.exists ():
		url = 'http://ftp.uk.debian.org/debian/dists/stable/main/Contents-'+input+'.gz'
		wget.download(url, bar='')

# Used to extract the .gz file
def extractor(input): 
	# first check if it exists, if it does, then we skip this
	file = pathlib.Path('./Contents-'+input)
	if not file.exists ():
		with gzip.open('./Contents-'+input+'.gz', 'rb') as f_in:
			with open('Contents-'+input, 'wb') as f_out:
				shutil.copyfileobj(f_in, f_out)	
				
				
				
############################################################################
#                             Main Function                                #
############################################################################

arch=""
try: 
	arch = sys.argv[1] # only want the first input
except:
	# If the user did not input something, they will know  
	print("Please enter an archtecture whilst running the program")
	print("EXAMPLE RUN: $ ./package_statistics.py <architecture name> ")
	quit()
	
# First we check if a valid architecture was given
checkArch(arch)

# Now we will fetch the Contents-arch
fetcher(arch)
	
# Now we extract the package, but first check if it exists
extractor(arch)

# Now we put all the packages into a list
packageList = []
with open('./Contents-'+arch) as file_obj:
	reader_obj = csv.reader(file_obj)
	
	# Iterate each row of the contents file and add package to list
	for row in reader_obj:
		spaceIndex = row[0].rfind(" ")+1
		package = str(row[0][spaceIndex:])
		packageList.append(package)

# Make a dictionary with package and package count
packageDict = {}
for pack in packageList:
    if pack not in packageDict:
        packageDict[pack] = 1
    else:
        packageDict[pack] += 1
        
# Find top 10 packages, and print their values       
topPacks = (sorted(packageDict, key=packageDict.get, reverse=True)[:10])
for i in range(10): 
	spaceCount = (60-len(topPacks[i]))
	if(spaceCount < 0): 
		spaceCount=1
	print(topPacks[i]+" "*spaceCount+str(packageDict[topPacks[i]]))







