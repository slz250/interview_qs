def compute(s):
    substrs = set()
    for i in range(len(s) - 1):
        newSubstr = s[i]
        # print(newSubstr)
        substrs.add(newSubstr)
        for j in range(i + 1, len(s)):
            newSubstr += s[j]
            # print(newSubstr)
            substrs.add(newSubstr)
    substrs = sorted(substrs)
    # print(substrs)
    return substrs[len(substrs) - 1]


if __name__ == "__main__":
    print(compute("banana"))
