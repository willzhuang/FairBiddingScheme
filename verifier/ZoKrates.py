import os

def compile(filename):
    os.system("zokrates compile -i " + filename)
    return

def setup():
    os.system("zokrates setup")
    return		

def verify():
    os.system("zokrates export-verifier")
    return
