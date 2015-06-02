__author__ = 'od0236'

from redcap import Project, RedcapError
URL = 'http://redcap.dfdev.biz/redcap/api/'
API_KEY = 'B882733EE6C4FC181C7591DB30D07CF5'
project = Project(URL, API_KEY)

print (project.field_names)


import json
import fileinput

json_in = ""
for line in fileinput.input():
    json_in = json_in + line

json_in_dict = json.loads(json_in)

response = project.import_records(json_in_dict)

print (json_in_dict)