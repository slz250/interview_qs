class ZeroUtils(object):
    """
    next_swap = 0
    next_ele_swap = 1 (first non-zero)
    [0,1,0,3,12,0,14,15]
    next_swap = 1
    next_ele_swap = 3
    [1,0,0,3,12,0,14,15]
    next_swap = 2
    next_ele_swap = 12
    [1,3,0,0,12,0,14,15]
    next_swap = 3
    next_ele_swap = 14
    [1,3,12,0,0,0,14,15]
    """
    def moveZerosEnd(self, arr):
        zero_ptr_set = False
        nonzero_ptr_set = False
        zero_ptr = None
        nonzero_ptr = None
        #TODO: edge case check where no zeros or all zeros
        for i in range(len(arr)):
            if not zero_ptr_set and arr[i] == 0:
                zero_ptr = i
                zero_ptr_set = True
            elif not nonzero_ptr_set and arr[i] != 0:
                nonzero_ptr = i
                nonzero_ptr_set = True
        if not zero_ptr_set or not nonzero_ptr_set:
            return 1
        if zero_ptr < nonzero_ptr:
            nonzero_ptr = zero_ptr+1
        while nonzero_ptr < len(arr) and arr[nonzero_ptr] == 0:
            nonzero_ptr += 1
        if nonzero_ptr == len(arr):
            return 1

        while zero_ptr < len(arr) and nonzero_ptr < len(arr):
            self.swap(zero_ptr, nonzero_ptr, arr)
            zero_ptr += 1
            # while zero_ptr < len(arr) and arr[zero_ptr] != 0:
            #     zero_ptr += 1
            nonzero_ptr += 1
            while nonzero_ptr < len(arr) and arr[nonzero_ptr] == 0:
                nonzero_ptr += 1

        # for i in range(len(arr)-zero_ptr, len(arr), 1):
        #     self.swap(zero_ptr, i, arr)
        #     zero_ptr += 1

        return 0

    def swap(self, i, j, arr):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def moveZeroes(self, nums):
        if not nums or len(nums) == 0: return
        insert_pos = 0
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1

    def moveZeroes1(self, nums):
        n = len(nums)
        num_zeroes = 0
        for i in range(n):
            if nums[i] == 0:
                num_zeroes += 1
        ans = []
        for i in range(n):
            if nums[i] != 0:
                ans.append(nums[i])
        while num_zeroes != 0:
            ans.append(0)
            num_zeroes-=1
        for i in range(n):
            nums[i] = ans[i]

    def moveZeroes2(self, nums):
        lastNonZeroFoundAt = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZeroFoundAt] = nums[i]
                lastNonZeroFoundAt += 1
        for i in range(lastNonZeroFoundAt, len(nums)):
            nums[i] = 0

    def moveZeroes3(self, nums):
        lastNonZeroFoundAt = 0
        for cur in range(len(nums)):
            if nums[cur] != 0:
                self.swap(lastNonZeroFoundAt, cur, nums)
                lastNonZeroFoundAt += 1

    def swap(self,i,j,li):
        temp = li[i]
        li[i] = j
        li[j] = temp

def moveZeros(nums):
    #go thru nums if 0 don't swap
    #init insert_idx to 0
    #if non-zero swap w/ insert_idx then
    #update insert_idx
    #from insert_idx to end change to 0
    #
    #if zero don't swap b/c it needs to be replaced
    #if non-zero swap b/c it'll go into where a 0 is
    pass

if __name__ == '__main__':
    sol = ZeroUtils()
    arr = [0,0,0,3,12,0,0,1]
    sol.moveZerosEnd(arr)
    print(arr)

