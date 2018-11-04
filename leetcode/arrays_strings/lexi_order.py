class Solution(object):
    def lexi_order_iter(self, N):
        curr, count = 1, 0
        while count != N:
            while curr <= N:
                print(curr)
                curr *= 10
            curr = int(curr/10)
            # curr = math.floor(curr / 10)
            last_digit = curr % 10
            while last_digit == 9:
                curr = int(curr / 10)
                last_digit = curr % 10
            curr += 1
            count += 1

if __name__ == '__main__':
    sol = Solution()
    sol.lexi_order_iter(200)