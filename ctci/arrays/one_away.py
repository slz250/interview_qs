import math

def one_away(str1, str2):
    i = 0
    j = 0

    error = False
    """
    here my logic is kind of getting mixed together
    in that case, let's try separating the logic into separate methods
    """
    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j] and i + 1 != len(str1) and j + 1 != len(str2):
            if str1[i + 1] == str2[j]:
                if error:
                    return False
                error = True
                i += 1
            elif str1[i] == str2[j + 1]:
                if error:
                    return False
                error = True
                j += 1
            elif str1[i + 1] == str2[j + 1]:
                if error:
                    return False
                error = True
                i += 1
                j += 1
            else:
                if error:
                    return False
                error = True

        i += 1
        j += 1

    return True

def one_away_ans(str1, str2):
    pass
if __name__ == '__main__':
    print(one_away('pale', 'ale'))
    print(one_away('pales', 'pale'))
    print(one_away('pale', 'bale'))
    print(one_away('pale', 'bake'))
    print('\n')
    print(one_away('shi', 'shai'))
    print(one_away('aaaaaa', 'baaaaa'))
    print(one_away('abcde', 'abde'))
    print(one_away('shey', 'shai'))