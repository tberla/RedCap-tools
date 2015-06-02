__author__ = 'Tim Berla'

import sys

print ('Number of arguments:', len(sys.argv), 'arguments.')
print  ( 'Argument List:', str(sys.argv[0]) )
print  ( 'Argument List:', str(sys.argv[1]) )



f = open(sys.argv[1], 'r')

str1 = f.read()

print (str1)

