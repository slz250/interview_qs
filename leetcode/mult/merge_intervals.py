def merge(intervals):
    intervals.sort(key=lambda x: x.start)

    merged = list()
    for interval in intervals:
        #if empty merged list or no overlap (prev's end is less than
        #curr's start)
        if not merged or merged[-1].end < interval.start:
            merged.append(interval)
        #overlaps so merge prev and curr
        else:
            merged[-1].end = max(merged[-1].end, interval.end)

    return merged


