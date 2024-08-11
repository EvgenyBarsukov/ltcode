s = "    fly me   to   the moon  "


def lengthOfLastWord(s: str) -> int:
    ss = s.strip()
    return len(ss.split()[-1])


print(lengthOfLastWord(s))