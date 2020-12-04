from itertools import combinations as getcombos
from itertools import starmap
from operator import add

def strippify(string=""):
  if isinstance(string,str):
    string = string.strip()
    return string

def dictify(tupkey,tupval):
  if isinstance(tupval,tuple) and len(tupval) == 2:
    return {int(tupkey): tupval}

with open('day_1-input.txt') as f:
  entries = list(f)
  entries = list(map(strippify,entries))
  entries = map(int,entries)

entrypairs = list(getcombos(entries,2))
entrysums = list(starmap(add,entrypairs))
entries = list(zip(entrysums,entrypairs))
entries = list(starmap(dictify,entries))

targetyear = 2020

def check2020(val):
  if isinstance(val,dict):
    for k in val.keys():
      if int(k) == targetyear:
        return True

result = filter(check2020,entries)
result = dict(next(result))[targetyear]
if len(result) == 2:
  result = result[0] * result[1]

print(result)
