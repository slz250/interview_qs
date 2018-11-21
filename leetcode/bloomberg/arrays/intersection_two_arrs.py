class ArrayUtils(object):
    def intersection(self, arr1, arr2):
        arr1_set = set(arr1)
        arr2_set = set(arr2)
        res = []
        if len(arr2_set) <= len(arr1_set):
            for ele in arr2_set:
                if ele in arr1_set:
                    res.append(ele)
        else:
            for ele in arr1_set:
                if ele in arr2_set:
                    res.append(ele)
        return res