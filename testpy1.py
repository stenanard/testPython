#! /usr/bin/env python
""" An example of python script
    Note that
"""
import sys # Load the system library

def main_function(parameter):
    print "here is where we do the stuff"
    print parameter
    parameter = parameter

    return parameter


if __name__ == "__main__":
    param = sys.argv[1]
    result = main_function(param)	
    print "Hello Steph"
    print result

    if result > 0:
        print result
    elif result == 0:
        print 0
    else:
        print "Not so good"

    for item in [ 'spam1' , 'spam2' , 'spam3' , 'spam4' ]:
        print item

    counter=5
    while counter > 0:
        print counter
        counter -= 1

    for i in range(3):
        print i
    
