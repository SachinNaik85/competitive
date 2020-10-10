def getval(string):
    dix = {}
    for i in range(len(string)):
        try:
            if dix[string[i]]:
                dix[string[i]].append(i)
        except KeyError:
            dix[string[i]] = [i]
    return sorted([i for i in list(dix.values()) if len(i) > 1])


def isIsomorphic(s, t):
    return True if getval(s) == getval(t) else False


def isIsomorphic1(s, t):
    sdix = {}
    tdix = {}
    for i in range(len(s)):
        if s[i] in sdix:
            if sdix[s[i]] != t[i]:
                return False
        elif t[i] in tdix:
            return False
        else:
            sdix[s[i]] = t[i]
            tdix[t[i]] = s[i]
    return True


if __name__ == '__main__':
    print(isIsomorphic1(input('Enter first string : '), input('Enter second string : ')))

"""
paper -> p : [0, 2] a : [1] e : [3] r : [4]
title -> t : [0, 2] i : [1] l : [3] e : [4]

add -> a : [0] d : [1, 2] 
egg -> e : [0] g : [1, 2]

foo -> f : [0] o : [1, 2]
bar -> b : [0] a : [1] r : [2]

book -> b : [0] o : [1, 2] k : [3]
sads -> a : [1] d : [2] s : [1, 3]
 
"""