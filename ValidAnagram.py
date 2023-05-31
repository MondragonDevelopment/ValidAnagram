s1 = "anagram"
s2 = "nagaram"

def isAnagram(s, t):
    # This is the same as using:
    # return Counter(s) == Counter(t)
    # but this maybe won't be useful in an interview

    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False

    return True

x = isAnagram(s1, s2)

print(x)