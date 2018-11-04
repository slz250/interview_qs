class Solution:
    """
    bf:
    1) create every substr
    2) for each substr:
            find max length
            for each char in substr:
                for each other char1 in substr:
                    check if char == char2:
                        return False

    eff:
    Input: "a b c a b c b b"
            0 1 2 3 4 5 6 7

    count = [2,4,2,2,4,2,4,4]
    we can get this in O(n) w/ hashmap where
    K = char and V = [list of indices this char appears in]

    ***longest_poss_till_next = [3,4,5,-1,6,-1,7,-1]***

    pseudocode:
    def sol(str):
        hm = hashmap()
        for i in 0..n:
            if str[i] is not in hm:
                hm.put(str[i],[i])
            else:
                list = hm.get(str[i]
                list.append(i)

        #iteration thru map is O(n)

        for char in longesT_poss_till_next:


    """
    def longest_substr_no_repeat_bf(self, str_):
        n = len(str_)
        max_ = 1
        """
        O(n^3) b/c for each of the substrs made from O(n^2)
        we have to iterate by a count of n
        """
        for i in range(0, n - 1):
            for j in range(i, n):
                if self.is_unique(str_, i, j):
                    max_ = j - i if max_ < j - 1 else max_
        return max_

    def is_unique(self, str_, i, j):
        uniques = set()
        for x in range(i, j + 1):
            if str_ in uniques:
                return False
            uniques.add(str_[x])
        return True

    """
    sliding window technique:
    window bounds are [i, j)
    i = 0, j = 0
    keep increasing j and store arr[j] into set as long as
    arr[j] is not already in set --> increasing window size
    (we are trying to optimize window size)
    
    if arr[j] is in set then we begin decreasing window size 
    on i side by increasing i (aka removing arr[i] from substr
    or set) until we find that arr[j] is no longer in set
    at which point we add arr[j] and continue
        we know that at this point the uniqueness principal is still 
        maintained b/c what was unique before will still be unique now within
        that window
    """
    def longest_substr_no_repeat_lt(self, str_):
        i = 0
        j = 0
        uniques = set()
        n = len(str_)
        max_ = 0
        while j < n:
            if str_[j] in uniques:
                uniques.remove(str_[i])
                i += 1
            else:
                temp = j - i + 1
                uniques.add(str_[j])
                j += 1
                max_ = temp if temp > max_ else max_
        return max_

    def longest_substr_no_repeat_lt1(self, str_):
        i = 0
        j = 0
        uniques = {}
        n = len(str_)
        max_ = 0
        while j < n:
            if str_[j] in uniques:
                """
                we find the max btwn the index of last
                repeat and current i b/c if we've already 
                passed the index of last repeat then we can't
                go back and reinclude it
                """
                i = max(uniques[str_[j]] + 1, i)
            else:
                temp = j - i + 1

            uniques[str_[j]] = j
            max_ = temp if temp > max_ else max_
            j += 1
        return max_