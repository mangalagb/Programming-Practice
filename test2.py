from collections import OrderedDict

def subStringsKDist(inputStr, num):
    # WRITE YOUR CODE HERE
    if len(inputStr) == 0:
            return 0
    elif len(inputStr) == 1:
        return 1

    result = set()
    for i in range(0, len(inputStr) - num+1):
        unique_characters = OrderedDict()

        for j in range(i, i+num):
            unique_characters[inputStr[j]] = 1

        if len(unique_characters) == num:
            str = ""
            for key, value in unique_characters.iteritems():
                str = str + key
            result.add(str)

    return list(result)


s = "awaglknagawunagwkwagl"
k = 4
subStringsKDist(s, k)