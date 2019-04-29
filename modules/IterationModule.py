# lst rules
# str sinput
# return lst
def doIteration(rules, sinput):
    flag = True
    i = 0
    for rule in rules:
        if (sinput.find(rule[0]) != -1):
            flag = False
        stmp = sinput.replace(rule[0], rule[1], 1)
        if (not flag):
            sinput = stmp
            if (rule[2]):
                flag = True
                break
            break
        i += 1
    return [sinput, flag, i]
