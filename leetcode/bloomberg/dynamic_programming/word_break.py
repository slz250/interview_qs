import time, queue
"""
recognize that the problem requires to try out all different combinations
therefore we should probably use DP

recur(i, j) --> word?
recur(0,i-1) + recur(i,j) + recur(j+1, n-1)

leetcode
l
le
lee
leet

e
ee
eet

wordDict: l ee tcode leet

see if any and all substrs are contained in wordDict
store as K-V pair: beg and end idx --> True/False

O(n^2)

see if any consecutive and non-overlapping segments
can be formed btwn 0 and n-1

separate problem above
0..12
0,4 0,5, 1,3 4,9 8,11 9,12

0,4 -> 4,9 -> 9,12

take range
recur on this range and see if theres connecting point
repeat this for all connecting points until
we have the whole range [0..n-1] covered

recur(start_mandate):
    if start_mandate == n-1:
        return True
    for range_ in ranges:
        if range_[0] == start_mandate:
            recur(range_[1])
    return False

O(n^2)

what about DP lol
we can have a table called poss_range[0..n-1]
that returns whether recur(start_mandate) has been
checked before..
==================================================
the problem is essentially asking is there a possible "cut"?
if there is then we can solve the problem recursively

go thru s and if accumulated substr is in wordDict
recur on the remaining substr
if we've hit end with match then return True
if we've hit w/o match return False

i.e:
applepenapple

['apple','pe','pen']
"""
def wordBreak(s, wordDict):
    def helper(s_):
        if s_ in dp_mem: return False
        for i in range(1, len(s_)+1):
            if s_[0:i] in wordDict:
                # print(f'i: {i} len(s)+1: {len(s_)+1} matched: {s_[0:i]}')
                if i == len(s_) or helper(s_[i:]):
                    # print(f'returning True for wordBreak({s_},..)')
                    return True
        # print(f'returning False for wordBreak({s_},..)')
        dp_mem.add(s_)
        return False

    dp_mem = set()
    start = time.time()
    res = helper(s)
    end = time.time()
    print('runtime: ', end-start)
    return res

def wordBreak1(s, wordDict):
    def word_Break(s, wordDict, start):
        if start == len(s):
            return True
        for end in range(start+1, len(s)+1):
            if s[start:end] in wordDict and word_Break(s, wordDict, end):
                return True
        return False
    return word_Break(s, set(wordDict), 0)

def wordBreak2(s, wordDict):
    wordDictSet = set(wordDict)
    q = queue.Queue()
    visited = [0 for i in range(len(s))]
    q.put(0)
    while not q.empty():
        start = q.get()
        if visited[start] == 0:
            for end in range(start+1, len(s)+1):
                if s[start:end] in wordDictSet:
                    q.put(end)
                if end == len(s):
                    return True
            visited[start] = 1
    return False

def wordBreak3(s, wordDict):
    wordDictSet = set(wordDict)
    dp = [False for i in range(len(s)+1)]
    dp[0] = True
    
    #substrs from 0 to i --> let's call it s1
    for i in range(1, len(s)+1):
        #substrs of s1
        for j in range(i):
            if dp[j] and s[j:i] in wordDictSet:
                dp[i] = True
                break
    return dp[len(s)]


if __name__ == '__main__':
    # s = 'catsandog'
    # wordDict = ['cats', 'dog', 'sand', 'and', 'cat']
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    res = wordBreak(s, wordDict)
    print(res)