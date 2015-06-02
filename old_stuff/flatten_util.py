__author__ = 'Tim Berla'

import json
import fileinput
import pprint
import flattener
import sys


if ( len ( sys.argv) == 2):
    print ( "flatten_util.py, config file = " , sys.argv[1], " input - stdin")
elif( len ( sys.argv) == 3):
    print ( "flatten_util.py, config file = " , sys.argv[1], " input file = ", sys.argv[2])
else:
    print ( "flatten_util.py, illegal arguments: " , sys.argv)
    sys.exit(-1)

config_file = open(sys.argv[1], "r")
config_str = config_file.read()
config = json.loads(config_str)


json_file = open(sys.argv[2], "r")
json_str = json_file.read()
json_in_dict = json.loads(json_str)

#json_in = ""
#       for line in fileinput.input():
#       json_in = json_in + line

#json_in_dict = json.loads(json_in)


out_list = flattener.flatten_json_dict( json_in_dict )

pp = pprint.PrettyPrinter(indent=4, width = 200)
pp.pprint(out_list)








