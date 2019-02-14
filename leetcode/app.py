def test():
    intervals = [(0,3),(0,4),(0,2)]
    intervals.sort(key=lambda x: x[0])
    print(intervals)

if __name__ == '__main__':
    test()