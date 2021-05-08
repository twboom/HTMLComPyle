import sys
import os
import shutil

# Compile the files
# Returns HTML as string
def compilePage(path):
    output = []
    files = []
    file = open(path, 'r').readlines()
    file = [i.strip() for i in file]
    if file[0].lower() != '<!doctype html>': print(f'The first line of {path} is not a (valid) HTML5 doctype declaration.')
    for line in file:
        if line == '': continue # Skip if line is empty
        if 'compyle' in line:
            line = line.replace("<compyle ", '')
            line = line.replace("/>", '')
            line = line.replace('"', '')
            line = line.split("=")
            files.append(line[1])
            if line[0] == 'script': line = f'<script src="{line[1]}"></script>'
            if line[0] == 'css': line = f'<link rel="stylesheet" href="{line[1]}">'
            output.append(line)

        else: output.append(line)

    return {
        'lines': output,
        'files': files
    }


# Get the files to compile
# Returns list of path (e.g. ['pages/index.html', 'pages/about.html'])
def getFile(dir):
    struct = dir.split('/')

    name = struct[-1] # Filename and extension
    del struct[-1] # Folders in a list

    files = []

    path = '/'
    path = path.join(struct) # Folders in a strings, seperated with a '/'

    # Get all files if all files of directory are required
    if name.split('.')[0] == '*':
        for file in os.listdir(path):

            # Check if path is a directory
            if os.path.isdir(f'{path}/{file}'): continue

            # Error if file extension is not HTML
            if file.split('.')[-1] != 'html':
                print(f'The file {path}/{file} does not have the HTML extension, the build will continue. There might be errors in the output.')
            
            files.append(file)
    else:
        files.append(name)

    return [f'{path}/{this}' for this in files]


# Export the files to the output folder
def exportPage(content, location, name):

    try:
        shutil.rmtree(location)
    except:
        pass

    os.makedirs(location, exist_ok=True)



# Importing the list of pages to generate
pages = open('pages.config', 'r').readlines()
pages = [i.strip() for i in pages]

exportPage(compilePage('pages/index.html'), 'output', 'index.html')