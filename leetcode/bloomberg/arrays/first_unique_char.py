class ArrayUtils(object):
    def firstUniqChar(self, s):
        """
        hm -> char to count
        first pass: get hm
        second pass: get res

        can we do it in one pass?
        ordered hm? --> linkedhashmap

        need to get counts first
        :param s:
        :return:
        """
        if not s:
            return -1
        char_count = dict()
        for c in s:
            if c not in char_count:
                char_count[c] = 1
            else:
                char_count[c] += 1

        for i in range(len(s)):
            if char_count[s[i]] == 1:
                return i

        return -1