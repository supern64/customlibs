# PythonFileManager
# A high level API for interacting with text files
# THIS LIBRARY WAS REVAMPED FOR PUBLIC RELEASE AND HAS NOT BEEN TESTED. PLEASE CONTACT SUPERNIINTENDO IF YOU FIND ANY BUGS.

import os
import shutil

def write(content, file):
    """Writes to a file.
    Arguments:
        content: The content of the file to write.
        file: The filename of the file to write to"""
    file  = open(file, 'w+')
    file.write(content)
    file.close()

def read(file):
    """Reads and returns the content of a file."""
    file  = open(file, 'r')
    output = file.read()
    return output

def log(content, file):
    """Appends to a file.
    Arguments:
        content: The content of the file to write.
        file: The filename of the file to write to"""
    file  = open(file, 'a')
    file.write(content)
    file.close()

def delete(file):
    """Deletes a file.
    Arguments:
        file: The filename of the file to delete."""
    os.remove(file)

def files(dir="./"):
    """Lists all files in a certain directory.
    Arguments:
        dir: The directory to write to. Defaults to the working directory."""
    lists = os.listdir(dir)
    return lists

def makedir(name):
    """Makes a new directory.
    Arguments:
        name: The name of the folder to make.
    Raises:
        ValueError: Directory already exists."""
    if not os.path.exists(name):
        os.makedirs(name)
    else:
        raise ValueError("Directory already exists.")

def deldir(name):
    """Deletes a directory.
    Arguments:
        name: The name of the folder to delete.
    Raises:
        ValueError: Directory doesn't exists."""
    if not os.path.exists(name):
        raise ValueError("Directory does not exist.")
    else:    
        shutil.rmtree(name)
 
def rename(oldname, newname):
    """Renames a file.
    Arguments:
        oldname: The file's name.
        newname: The file's new name. (Can be another directory to move file.)"""
    os.rename(oldname, newname)

def copy(file, directory):
    """Copies a file.
    Arguments:
        file: The file name to copy.
        directory: The directory to copy to."""
    shutil.copy(file, directory)
