__author__ = 'Tim Berla'

import json
import fileinput
import pprint
import flattener
import sys
import pymssql
import datetime

print ( sys.argv)

if ( len ( sys.argv) == 2):
    print ( "sql_to_redcap.py, config file = " , sys.argv[1])
else:
    print ( "sql_to_redcap.py, illegal arguments: " , sys.argv)
    sys.exit(-1)

config_file = open(sys.argv[1], "r")
config_str = config_file.read()
config = json.loads(config_str)



conn = pymssql.connect ( host = config["sql-host"], user = config["sql-user"], password = config["sql-password"], database = config["sql-database"])
cur = conn.cursor()

print ( "Connected to host: " , config["sql-host"], " database: ", config["sql-database"])
cur.execute(config["sql-select-statement"])

field_list = config["redcap-fields"]
fixed_field_list = config["fixedFields"]
batch_count = int(config["batchCount"])

# if there is an idField specified in the config file, add it to all rows, incremented
if ("idField" in config):
    id_field = config["idField"]
    id_prefix = config["idPrefix"]
    process_id_field = True
else:
    process_id_field = False


out_rows = []
in_row = cur.fetchone()
if (len(field_list) != len(in_row)):
    print("Error: ", len(field_list), " objects in redcap-fields, ", len(in_row), " objects in fetched table row")
while in_row:
    i = 0
    out_row = {}
    if ( process_id_field ):
        out_row[id_field] = ( id_prefix + str(len(out_rows) + 1))
    for field_name in field_list:
        if (isinstance(in_row[i], str)):
            val_str = in_row[i]
        else:
            val_str = in_row[i].strftime("%Y-%m-%d %H:%M:%S")
        out_row[field_name] = val_str
        i += 1
    out_row.update( fixed_field_list )
    out_rows.append(out_row)
    in_row = cur.fetchone()

print ( "Read ", len(out_rows), " records from sql database: ", config["sql-database"] )

conn.close()

from redcap import Project, RedcapError
URL = (config["redcapURL"])
API_KEY = (config["redcapApiKey"])
project = Project(URL, API_KEY)


batch_start = 0
while ( batch_start < len(out_rows)):
    response = project.import_records(out_rows[batch_start : batch_start + batch_count])
    if ( batch_start + batch_count <= len(out_rows)):
        print ("Added a batch of ", batch_count, " records")
    else:
        print ("Added a batch of ", len(out_rows) - batch_start, " records")
    batch_start += batch_count

