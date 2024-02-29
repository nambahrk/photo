from pathlib import Path
import sys

def tojpg():
    for f in Path('.').rglob('*.png'):
        f.rename(f.stem+'.jpg')
    for f in Path('.').rglob('*.jpeg'):
        f.rename(f.stem+'.jpg')

def topng():
    for f in Path('.').rglob('*.jpg'):
        f.rename(f.stem+'.png')
    for f in Path('.').rglob('*.jpeg'):
        f.rename(f.stem+'.png')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extension.py extension")
        print("Valid operations: tojpg topng")
    else:
        operation = sys.argv[1]

        if operation == "tojpg":
            tojpg()
        elif operation == "topng":
            topng()       
        else:
            print("Invalid operation. Valid operations: tojpg topng")

