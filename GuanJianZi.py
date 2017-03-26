import os

def find_key(path,key):
    for roots,dirs,files in os.walk(path):
        print roots
        print dirs
        print files

find_key(r'C:\Python27\lib','')