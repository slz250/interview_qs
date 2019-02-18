class Solution(object):
    """
    bf
    ================================================
    go thru each substr of length of p
    check if anagram by:
        -have a hashmap to count frequency of letters
        -initialize hashmap w/ letter counts of p where
        k -> letter v -> count
        -go thru substr and if char is not in hashmap then
        not an anagram
        -else decrease the count and if curr count is already 0
        also not an anagram
        -True if we've reached this point and remember to store
        beginning index

    sliding window
    ================================================
    -sliding window substr of length of p
    -list letter_counts of size 26 where idx 0 = a, 1 = b, etc
    -@ each sliding window check if letter_counts matches counts of p
        T -> anagram F -> not anagram
    -move from left to right by removing beginning char and decrementing
    count in letter_count and adding next char as ending char and increasing
    count in letter_count
    -a lot less operations than above
    """

    def initLetterCountsDict(self, p):
        letter_counts = dict()

        for c in p:
            if c not in letter_counts:
                letter_counts[c] = 1
            else:
                letter_counts[c] += 1

        return letter_counts

    def checkAnagram(self, substr, letter_counts):
        # print(f'substr: {substr}')
        for c in substr:
            if c not in letter_counts:
                return False
            elif letter_counts[c] == 0:
                return False
            else:
                letter_counts[c] -= 1

        return True

    def findAnagrams(self, s, p):
        res = list()
        if not s or not p: return res

        letter_counts = self.initLetterCountsDict(p)
        # print(f'len(s): {len(s)}, len(p): {len(p)}')
        # print(f'ending i: {len(s)-len(p)+1}')
        # print(f'starting j: {len(p)-1}')
        for i in range(len(s) - len(p) + 1):
            temp = letter_counts.copy()
            if self.checkAnagram(s[i:i + len(p)], temp):
                # print('found anagram')
                res.append(i)

        return res

    def findAnagrams1(self, s, p):
        pass

    def test(self):
        s = 'cbaebabacd'
        p = 'abc'
        res = self.findAnagrams(s, p)
        print(res)


if __name__ == '__main__':
    sol = Solution()
    sol.test()
