#!/usr/bin/python
import os, sys

#get location of the files
currpath = raw_input("Enter the absolute path to directory: ")

#go to the directory specified by user
os.chdir(currpath)

#print all the files in that directory for ease of use
files = os.listdir(currpath)
for f in files:
    print f

#text to be removed from the end of the string
remStr = raw_input("Enter the common string to be removed from the end exactly: ")
lenRemStr = len(remStr) * -1

#get file extension and length
ext = raw_input("File extension: ")
lenExt = len(ext) * -1

for f in files:

    #get the string without the extension into f1
    f1 = f[:lenExt]

    #if f1 contains the string to be removed at the end after removal of extension
    if f1.endswith(remStr):

        #strip the text to be removed
        f1 = f1[:lenRemStr]
        f1.rstrip()

        #add the extension back
        f1 += ext

        #print for user to verify
        print f1

        #if user is now satisfied, the name is changed
        consent = raw_input("Go ahead? (y/n) ")
        if consent == 'y':
            os.rename(f, f1)
        else:
            continue

print "Done!"
