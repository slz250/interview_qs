class Solution(object):
    """
    ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e","e"]
    ["b","l","u","e","e", " ", "i","s", " ", "s","k","y"," ","t","h","e"]

    ["b","l","u","e","s","k","y"," ","i","s"," "," "," ", t","h","e"]

    swap(leftWordIdx, rightWordIdx):


    insert and shift

    get start & end index of left_word and right_word
    from end_index to start_index (left) swap with start_index to end_index (right)
    current word idea

    if either word is not finished, look for other next word and if next word is within the range
    of first_unfinished word continue
    """
    def reverseWords(self, s):
        def reverse(i, j):
            while i < j:
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                i+=1
                j-=1

        if len(s) == 0:
            return
        start_i = 0
        for i in range(len(s)):
            if s[i] == ' ':
                reverse(start_i, i-1)
                start_i += 1
        reverse(start_i, len(s)-1)

        reverse(0, len(s)-1)
        return s