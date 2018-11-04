def string_compression(str_):
    res = ""
    prev = str_[0]
    count = 0
    for letter in str_:
        if letter == prev:
            count += 1
        else:
            res += prev
            res += str(count)
            count = 1
        prev = letter

    res += prev
    res += str(count)

    print(res)
    if len(res) > len(str_):
        return str_
    else:
        return res

if __name__ == "__main__":
    print(string_compression("aabcccccaaa"))