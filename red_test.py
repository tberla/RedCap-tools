__author__ = 'od0236'

import redcap

from redcap import Project



l = [ { "a" : 1, "b" : "tooth"},{ "a" : 2, "b" : "biscuit"},{ "a" : 1, "b" : "banana"},{ "a" : 4, "b" : "straw"},{ "a" : 1, "b" : "beer"},{ "a" : 1, "b" : "gritz"}, ]

ll = [item for item in l if item["a"] == 1]


tureky = "gobble"