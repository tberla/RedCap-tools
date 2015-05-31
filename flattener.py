__author__ = 'Tim Berla'

import copy
import re


def flatten_json_dict (the_input_dict, add_dFpath, dFpath_field, add_record_id, record_id_field, record_id_prefix):

    record_index = 1
    out_dict = {}

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
                        joint_value = joint_value + "|" + str_val
                    local_vals.update({the_key:  joint_value[1:]})
                else:
                    lists.append(thing)
                    is_terminal = False
            elif ( the_value is not None ):                 # if null, just jeave this attribute out
                if isinstance(the_value, str):
                    if re.search(r"\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ", the_value):
                        the_value = the_value[:10] + " " + the_value[11:19]
                local_vals.update( {the_key: the_value})

        if ( is_terminal ):
            dFpath_val = prefix[1:]
            if add_dFpath:
                local_vals.update({dFpath_field: dFpath_val})

            nonlocal record_index;

            if add_record_id:
                local_vals[record_id_field] = record_id_prefix + str(record_index)
                record_index += 1
            if dFpath_val in out_dict:
                out_dict[dFpath_val].append(local_vals)
            else:
                out_dict[dFpath_val] = [local_vals]
        else:
            for it in dicts:
                parse_json_dict(prefix + "|" + it[0], local_vals, it[1])
            for it in lists:
                for it2 in it[1]:
                    parse_json_dict(prefix + "|" + it[0], local_vals, it2)





    parse_json_dict("", {}, the_input_dict)

    return out_dict
