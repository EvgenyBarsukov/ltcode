haystack = "leetcode"
needle = "leeto"

def strStr(haystack: str, needle: str) -> int:
    out = -1
    if needle in haystack:
        out = haystack.index(needle)
    return out
    return haystack.index(needle)


print(strStr(haystack, needle))