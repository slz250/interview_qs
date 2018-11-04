import math

class Solution(object):
    def lexi_order(self, num):
        lists = [[i] for i in range(10)]
        #to get first digit
        divisor = 10
        for x in range(10, num):
            divisor = divisor * 10 if x == divisor * 10 else divisor
            idx = math.floor(x / divisor)
            lists[idx].append(x)

        # print(lists[1])
        # print(lists[2])
        for i in range(1, len(lists)):
            for x in lists[i]:
                print(x)

    # Python program to sort the words in lexicographical
    # order

    def sortLexo(self, N):
        li = []
        for i in range(1, N):
            li.append(str(i))
        li.sort()
        for x in li:
            print(x)

if __name__ == '__main__':
    sol = Solution()
    # sol.lexi_order(200)
    sol.sortLexo(200)