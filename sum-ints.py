# Wesley Murray
# 2/9/2020
# This script is meant to sum a range of numbers

#import libraries
import sys

#constants
START = 0
STOP = 0

#validate command line args
def commandLineArgValidation():
    #check for two arguments
    if(len(sys.argv)!=3):
        return "Error: Only provide two arguments."

    #validate arg type
    try:
        START = int(sys.argv[1])
        STOP = int(sys.argv[2])
    except ValueError:
        return "Error: The provided arguments are not integers."

    #validate order
    if(START>STOP):
        temp = START
        START = STOP
        STOP = temp

    return None

def main():
    commandLineArgValidation()

main()