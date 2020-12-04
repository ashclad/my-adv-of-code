# PT 1

def strippify(string):
  string = string.strip()
  return string

def dictify(a):
  if isinstance(a,str):
    if ": " in a:
      templist = a.split(": ")
    elif ":" in a:
      templist = a.split(":")

    if len(templist) == 2:
      return {"policy": templist[0], "pwd": templist[1]}

with open('day_2-input.txt','r') as entries:
  entries = list(entries)

entries = list(map(strippify,entries))
entries = list(map(dictify,entries))

def testrule(ruleset):
  if isinstance(ruleset,dict):
    rule = ruleset['policy'].split(' ')
    target = rule[1]
    if '-' in rule[0]:
      rule = rule[0].split('-')
      rule = [int(rule[0]), int(rule[1])]
      rule.sort()
      rulestart = rule[0]
      ruleend = rule[1]
    else:
      rule = int(rule[0])

    if isinstance(rule,list):
      if len(rule) == 2:
        if ruleset['pwd'].count(target) >= rulestart and ruleset['pwd'].count(target) <= ruleend:
          return ruleset['pwd']
    elif isinstance(rule,int):
      if ruleset['pwd'].count(target) == rule:
        return ruleset['pwd']

entries = list(map(testrule,entries))
entries = list(filter(lambda x: False if x is None else True,entries))

# PT 2

with open('day_2-input.txt','r') as same_entries:
  same_entries = list(same_entries)

same_entries = list(map(strippify,same_entries))
same_entries = list(map(dictify,same_entries))

def diff_testrule(ruleset):
  rule = ruleset['policy'].split(' ')
  target = rule[1]
  if '-' in rule[0]:
    rule = rule[0].split('-')
    rule = [int(rule[0]), int(rule[1])]
    firstpos = rule[0]-1
    secpos = rule[1]-1
  else:
    rule = int(rule[0])

  if isinstance(rule,list) and len(rule) == 2:
    if ruleset['pwd'][firstpos] == target and not ruleset['pwd'][secpos] == target:
      return ruleset['pwd']
    elif not ruleset['pwd'][firstpos] == target and ruleset['pwd'][secpos] == target:
      return ruleset['pwd']

same_entries = list(map(diff_testrule,same_entries))
same_entries = list(filter(lambda x: False if x is None else True,same_entries))

firstlen = len(entries)
secondlen = len(same_entries)

print("Part 1: " + str(firstlen))
print("Part 2: " + str(secondlen))
