import sys
import os

# Compile the files
def compilePage(file):
    pass


# Get the files to compile
def getFile(dir):
    struct = dir.split('/')

    file = struct[-1] # Filename and extension
    del struct[-1] # Folders in a list

    path = '/'
    path = path.join(struct) # Folders in a strings, seperated with a '/'
    print(path)


# Export the files to the output folder
def exportPage(content, location, name, extension):
    pass



# Importing the list of pages to generate
pages = open('pages.config', 'r').readlines()
pages = [i.strip() for i in pages]

getFile(pages[0])