def getSortedList(names):
    numerals = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6,
                         "VII": 7, "VIII": 8, "IX": 9, "X": 10}
    tens = {"XX": 20, "XXX": 30, "XL": 40, "L": 50}

    names = sorted(names)
    """algo is to loop thru sorted names and then sort the duplicate
    names by roman numerals"""
    for i in range(len(names) - 1):
        for j in range(i + 1, len(names) - 1):
            pass

    return names

