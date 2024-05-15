# Package Statistics
## Introduction
Debian uses *.deb packages to deploy and upgrade software. 
The packages are stored in repositories and each repository contains a so called "Contents Index". 
The format of that file is well described: [here](https://wiki.debian.org/RepositoryFormat#A.22Contents.22_indices)

## Project Description
For your assignment, you are to develop a python command line tool that takes the architecture (amd64, arm64, mips etc.) as an argument and downloads the compressed contents file associated with it from a Debian mirror. 
The program should parse the file and output the statistics of the top 10 packages that have the most files associated with them.
 
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

 ## Credit
 This question was found [here](https://www.glassdoor.co.uk/Interview/python-telecom-engineer-interview-questions-SRCH_KO0,23.htm)
 This is simply my crackk at it
