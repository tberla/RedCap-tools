__author__ = 'Tim Berla'

import json
import copy
import fileinput
import pprint

def parse_json_dict(prefix, vals, the_dict):
    local_vals = copy.deepcopy(vals)
    item_list = the_dict.items()
    is_terminal = True
    dicts = []
    lists = []
    for thing in item_list:
        the_key = thing[0]
        the_value = thing[1]
        if (isinstance(the_value, dict)):
            dicts.append(thing)
            is_terminal = False
        elif (isinstance(the_value, list)):
            if ( len ( the_value ) == 0):
                pass   #       for  '"key" = []" we just leave out that key -- local_vals.update({the_key:  ""})
            elif (isinstance(the_value[0], str)):
                joint_value = ""
                for str_val in the_value:
                    joint_value = joint_value + "|" + str_val;
                local_vals.update({the_key:  joint_value[1:]})
            else:
                lists.append(thing)
                is_terminal = False
        elif ( the_value is not None ):                 # if null, just jeave this attribute out
            local_vals.update( {the_key: the_value})

    if ( is_terminal ):
        local_vals.update({"dFpath": prefix[1:]})
        out_list.append(local_vals)
    else:
        for it in dicts:
            parse_json_dict(prefix + "|" + it[0], local_vals, it[1])
        for it in lists:
            for it2 in it[1]:
                parse_json_dict(prefix + "|" + it[0], local_vals, it2)

json_in = ""
for line in fileinput.input():
    json_in = json_in + line

json_in_dict = json.loads(json_in)

out_list = []

parse_json_dict("", {}, json_in_dict)

pp = pprint.PrettyPrinter(indent=4, width = 200)
pp.pprint(out_list)
