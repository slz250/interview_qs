class ArrUtils(object):
    def thirdMax(self, arr):
        max1 = max2 = max3 = None
        for num in arr:
            if num == max1 or num == max2 or num == max3:
                continue
            if not max1 or num > max1:
                temp = max1
                temp1 = max2
                max1 = num
                max2 = temp
                max3 = temp1
            elif not max2 or num > max2:
                temp = max2
                max2 = num
                max3 = temp
            elif not max3 or num > max3:
                max3 = num

        return max3 if max3 is None else max1