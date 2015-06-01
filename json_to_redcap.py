__author__ = 'Tim Berla'

import json
import fileinput
import pprint
import flattener
import sys


if ( len ( sys.argv) == 3):
    print ( "json_to_redcap.py, config file = " , sys.argv[1], " input file = ", sys.argv[2])
else:
    print ( "json_to_redcap.py, illegal arguments: " , sys.argv)
    sys.exit(-1)

#   config_file = open(sys.argv[1], "r")
#   config_str = config_file.read()
#   config = json.loads(config_str)
config = json.load(open(sys.argv[1], "r"))

if "idField" in config:
    add_record = True
    record_id_field = config["idField"]
    record_id_prefix = config["idPrefix"]
else:
    add_record = False
    record_id_field = ""
    record_id_prefix = ""

if "dFpathField" in config:
    add_dFpath = True
    dFpath_field = config["dFpathField"]
else:
    add_dFpath = False
    dFpath_field = ""


#   json_file = open(sys.argv[2], "r")
#   json_str = json_file.read()
#   json_in_dict = json.loads(json_str)
json_in_dict = json.load(open(sys.argv[2], "r"))

#json_in = ""
#       for line in fileinput.input():
#       json_in = json_in + line

#json_in_dict = json.loads(json_in)


out_rows = flattener.flatten_json_dict( json_in_dict, add_dFpath, dFpath_field, add_record, record_id_field, record_id_prefix )

pp = pprint.PrettyPrinter(indent=4, width = 200)
pp.pprint(out_rows)


import copy

from redcap import Project, RedcapError
URL = (config["redcapURL"])
batch_count = int(config["batchCount"])
df_path_map = (config["dfPathMap"])

for path in out_rows:
    record_set = out_rows[path]
    if path in df_path_map:
        api_key = df_path_map[path]
        project = Project(URL, api_key)
        print("Adding", len(record_set), "records for dFpath", path)
        batch_start = 0
        while ( batch_start < len(record_set)):
            response = project.import_records(record_set[batch_start : batch_start + batch_count])
            if ( batch_start + batch_count <= len(record_set)):
                print ("Added a batch of ", batch_count, " records")
            else:
                print ("Added a batch of ", len(record_set) - batch_start, " records")
            batch_start += batch_count
    else:
        print("Skipping", len(record_set), "records for dFpath", path)











