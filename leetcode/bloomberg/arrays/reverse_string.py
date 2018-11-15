class StringUtils(object):
    def reverse_string(self, s):
        s = list(s)
        i = 0
        j = len(s)-1
        while i < j:
            self.swap(i, j, s)
            i+=1
            j-=1
        return ''.join(s)

    def swap(self,i,j,s):
        temp = s[i]
        s[i] = s[j]
        s[j] = temp

if __name__ == '__main__':
    sol = StringUtils()
    print(sol.reverse_string('A man, a plan, a canal: Panama'))