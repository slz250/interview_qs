class ArrayUtils(object):
    def plusOne(self, num):
        """
        Input: [4, 3, 2, 1]
        Output: [4, 3, 2, 2]
        :param num:
        :return:
        """
        if not num:
            return num

        keep_going = True
        carry_over = False
        i = len(num)-1
        while i >= 0 and keep_going:
            if i == len(num)-1 or carry_over:
                temp = num[i] + 1
            if temp > 9:
                carry_over = True
                num[i] = 0
            else:
                num[i] = temp
                carry_over = False
            if not carry_over:
                keep_going = False
            i -= 1

        if carry_over:
            num.insert(0, 1)

        return num


if __name__ == '__main__':
    sol = ArrayUtils()
    li = [9,9,9,9]
    print(sol.plusOne(li))
