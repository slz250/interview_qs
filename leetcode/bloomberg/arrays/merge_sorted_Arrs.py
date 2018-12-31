def merge(nums1, m, nums2, n):
    #using concept of merge in merge sort
    #we go thru nums1 and nums2 and do comparisons of
    #the curr pos of each arr and place the larger one
    #in the back of nums1; we chose back of nums1 instead
    #doing vice-versa and replacing the front b/c the problem
    #going forward is that if we replace something in nums1
    #that hasn't been used then we need to store it somewhere (using extra storage)
    #to be used.
    i = m-1
    j = n-1
    k = m+n-1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i-=1
        else:
            nums1[k] = nums2[j]
            j-=1
        k -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        k-=1
        j-=1