def mySqrt(x):
    if not x:
        return None
    low = 1
    high = x
    while low <= high:
        mid = int((low + high)/2)
        print(f'low: {low} high: {high} mid: {mid}')
        print(f'prev^2: {prev*prev}')
        if mid*mid == x:
            return mid
        elif mid*mid < x < ((mid+1)*(mid+1)):
            return mid
        elif mid*mid > x:
            high = mid-1
        else:
            low = mid+1
    return None

def mySqrt1(x):
    if x == 0: return 0
    left, right = 1, x
    ans = None
    while left <= right:
        mid = left + (right-left) / 2
        if mid <= x / mid:
            left = mid+1
            ans = mid
        else:
            right = mid-1
    return ans

if __name__ == '__main__':
    x = 24
    res = mySqrt(x)
    print(res)