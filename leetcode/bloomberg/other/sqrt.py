def mySqrt(x):
    if not x:
        return None
    low = 0
    high = x
    prev = x
    while low <= high:
        mid = int((low + high)/2)
        print(f'low: {low} high: {high} mid: {mid}')
        print(f'prev^2: {prev*prev}')
        if mid*mid == x:
            return mid
        elif prev*prev < x < mid*mid:
            return prev
        elif mid*mid > x:
            high = mid-1
        else:
            low = mid+1
        prev = mid
    return None

if __name__ == '__main__':
    x = 24
    res = mySqrt(x)
    print(res)