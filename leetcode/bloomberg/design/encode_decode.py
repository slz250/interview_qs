class Codec:
    def encode(self, strs):
        if not strs:
            return None
        encoded = ''
        for s in strs:
            encoded += str(len(s)) + '/' + s
        print(encoded)
        return encoded


    def decode(self, s):
        if not s:
            return None
        i = 0
        strs = list()
        while i < len(s):
            slash = s.find('/', i)
            print(f'slash: {slash}')
            str_len = int(s[i:slash])
            print(f'str_len: {str_len}')
            str_ = s[slash+1:slash+str_len+1]
            print(f'str_: {str_}')
            strs.append(str_)
            i = slash+str_len+1
            print(f'i: {i}')
        return strs

if __name__ == '__main__':
    sol = Codec()
    strs = ['/o/ne','//two','three//']
    encoded = sol.encode(strs)
    decoded = sol.decode(encoded)
    print(decoded)
