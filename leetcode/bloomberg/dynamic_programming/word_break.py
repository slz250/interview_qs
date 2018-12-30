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
def workBreak(s, wordDict):
    pass