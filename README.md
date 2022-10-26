# Package Statistics
## Introduction
Debian uses *deb packages to deploy and upgrade software. The packages are stored in repositories and each repository contains the so called "Contents index". The format of that file is well described here https://wiki.debian.org/RepositoryFormat#A.22Contents.22_indices

## Project Description
Your task is to develop a python command line tool that takes the architecture (amd64, arm64, mips etc.) as an argument and downloads the compressed Contents file associated with it from a Debian mirror. The program should parse the file and output the statistics of the top 10 packages that have the most files associated with them. An example output could be:

 
## How to run the code
```bash
$ ./package_statistics.py amd64
```
 
## Output Example
```bash
$ ./package_statistics.py <architecture name> 
    <package name 1>         <number of files>
    <package name 2>         <number of files>
......
    <package name 10>        <number of files>
```
 
## Notes from Canonical
You can use the following Debian mirror: http://ftp.uk.debian.org/debian/dists/stable/main/. Please try to follow Python's best practices in your solution. Hint: there are tools that can help you verify your code is compliant. In-line comments are appreciated.

Please do your work in a local Git repository. Your repo should contain a README that explains your thought process and approach to the problem, and roughly how much time you spent on the exercise. When you are finished, create a tar.gz of your repo and submit it to the link included in this email. Please do not make the repository publicly available.

Note: We are interested not only in quality code, but also in seeing your approach to the problem and how you organize your work.

# Personal Notes
All text above is from Cannonical, whereas here I will be jotting down my thought process of how I want to achieve this task. After some quick brainstorming, here is how I plan to approach this project.

## Thought Process
1. Make a python script that will pull in a user input parameter
2. Check if the parameter is an architecture, if not, throw an error message
3. Fetch all the files from a specific package, this will be easy since all packages have the same name, just the architecture that follows them is different, so we will need to append the architecture to the url strings
4. Create a dictionary where the key is the package name, and the value will be the number of files associated with them. 
5. Make a set from the dictonary, then print the top ten dictonary elements with the highest results. 

## Timeline
This is a timeline of how long it took me to complete each of the following points listed above
- Brainstorm: 15min
- User input param: 3min
- Check input param: 15min
- File Fetcher based off input: 30min
- Files Dictionary & Organize the dictionary & Print top ten results: 25min 
	- These were all done together, and I lost track of time in between them 

Total Time: 1hr 28min

