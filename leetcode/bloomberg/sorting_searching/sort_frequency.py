"""
get counts
recreate string when highest count to lowest

counts hm
find min/max
bucket sort with arr of size range with
eles being chars themselves--> list of lists for
axcounting dups
"""
def frequencySort(s):
    if not s: return ''

    counts = dict()
    for c in s:
        if c not in counts:
            counts[c] = 1
        else:
            counts[c] += 1

    min_ = max_ = None
    for ele in counts:
        if not min_ and not max_:
            min_ = max_ = counts[ele]
        if counts[ele] < min_:
            min_ = counts[ele]
        elif counts[ele] > max_:
            max_ = counts[ele]

    # print(f'min: {min_}, max: {max_}')

    final = [[] for i in range(max_-min_+1)]
    for ele in counts:
        final[counts[ele]-min_].append(ele)

    # print(final)

    s = ''
    for i in range(len(final)-1,-1,-1):
        chars = final[i]
        # print(chars)
        for c in chars:
            # print(c)
            for j in range(i+min_):
                s += c
                # print(s)
    return s

if __name__  == '__main__':
    input_ = 'Aabb'
    output = frequencySort(input_)
    print(output)