class Solution(object):
    def __init__(self):
        self.next_swap = False
    """
    list of [a,b,c]

    permute(s, li):
        if len(li) == 0:
            print(s)
        for x in range(len(li)):
            temp = li.pop(x)
            permute(s+temp, li)
            li.add(x, temp)
    """

    """
    if we use linked list, runtime is constant for each call execution
    so time complexity = O(n^n)
    """
    def permutation(self, s, li):
        if len(li) == 0:
            print(s)
        for x in range(len(li)):
            temp = li.pop(x)
            self.permutation(s + temp, li)
            li.insert(x, temp)
    """
    abc swap a & a     acb
    bac swap a & b     bca
    cba swap a & c     cab
    """

    def permutation_swap(self, i, li):
        if i == len(li):
            print(li)
        for x in range(i, len(li)):
            self.swap(li, i, x)
            #next index to start swappinjg
            self.permutation_swap(i+1, li)
            self.swap(li, i, x)

    def swap(self, s, i, j):
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        # print(f'i:{i} j:{j} s:{s}')

    def driver(self, li):
        org = li.copy()
        li.sort()
        self.next_permutation(org, 0, li)
        print(li.sort())

    def next_permutation(self, org, i, li):
        """
        bf:
        generate every permutation
            if curr = s:
                print next
            if last_perm:
                print first
        sort in lexigraphical order
            -
        find curr s and return next one

        123 -> 132
        321 -> 123
        115 -> 151
        """
        if self.next_swap:
            print(li)
            exit(0)
        if i == len(li):
            if self.equals(org, li):
                self.next_swap = True
            return
        for x in range(i, len(li)):
            self.swap(li, i, x)
            #next index to start swappinjg
            self.next_permutation(org, i+1, li)
            self.swap(li, i, x)

    def equals(self, org, li):
        for i in range(len(org)):
            if org[i] != li[i]:
                return False
        return True

if __name__ == '__main__':
    sol = Solution()
    li = [3,2,1]
    sol.driver(li)
