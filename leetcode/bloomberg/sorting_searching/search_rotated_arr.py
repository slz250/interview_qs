def search(nums, target):
    left, right = 0, len(nums)-1
    mid = None

    while left <= right:
        mid = int((left+right)/2)
        if nums[mid] == target: return True
        if nums[left] == nums[mid] and nums[right] == nums[mid]:
            left += 1
            right -= 1
        #find the ascending part to allow for following check
        elif nums[left] <= nums[mid]:
            #if target is within this range (ascending) then
            #search within this range
            if nums[left] <= target and nums[mid] > target:
                right = mid-1
            #must be in other range
            else:
                left = mid+1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid+1
            else:
                right = mid-1
    return False
