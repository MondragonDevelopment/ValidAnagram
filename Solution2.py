s1 = "anagram"
s2 = "nagaram"

def isAnagram(s, t):
    # O(log N) orr O(1) space depending on the libraries used
    return sorted(s) == sorted(t)


x = isAnagram(s1, s2)

print(x)