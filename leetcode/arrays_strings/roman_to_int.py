class Solution(object):
    def roman_to_int(self, str_):
        if str_ == '' or None:
            return None

        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000

        }
        prev = mapping[str_[(len(str_) - 1)]]
        curr, res = prev, 0
        print(prev)
        for i in range(len(str_) - 2, -1, -1):
            curr = mapping[str_[i]]
            print(curr)
            if curr < prev:
                print('test')
                res -= curr
            else:
                print('test1')
                res += curr
            prev = curr
        return int(res)

if __name__ == '__main__':
    sol = Solution()
    # assert sol.roman_to_int('III') == 3
    # print(sol.roman_to_int('III'))
    # assert sol.roman_to_int('IV') == 4
    print(sol.roman_to_int('IV'))
    # assert sol.roman_to_int('IX') == 9
    # assert sol.roman_to_int('LVIII') == 58
    # assert sol.roman_to_int('MCMXCIV') == 1994
    # assert sol.roman_to_int('I') == 1
