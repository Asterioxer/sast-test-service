import os

def insecure(cmd):
    os.system(cmd)

insecure("ls")
